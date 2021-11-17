
import sqlite3
import inspect


SELECT_TABLE_SQL = "SELECT name FROM sqlite_master WHERE type = 'table';"
CREATE_TABLE_SQL = "CREATE TABLE {name}( {fields} );"
INSERT_TABLE_SQL = "INSERT INTO {name} ({fields}) VALUES ({placeholder});"
SELECT_TABLE_ALL_SQL = "SELECT {fields} FROM {name};"
SELECT_WHERE_SQL = "SELECT {fields} FROM {name} WHERE {query};"
SQLITE_TYPE_MAP = {
    int: "INTEGER",
    float: "REAL",
    str: "TEXT",
    bytes: "BLOB",
    bool: "INTEGER",
}


class Database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)

    def _execute(self, sql, data=None):
        if data is not None:
            return self.conn.execute(sql, data)
        return self.conn.execute(sql)

    @property
    def tables(self):
        return self._execute(SELECT_TABLE_SQL).fetchall()

    def all(self, table):
        return self._execute(table.get_all_table_sql()).fetchall()

    def create(self, table):
        self._execute(table.get_create_sql())

    def get(self, table, id):
        sql, fields, id = table.get_select_query(id=id)
        row = self._execute(sql, id).fetchone()
        data = dict(zip(fields, row))
        return table(**data)

    def _commit(self):
        self.conn.commit()

    def save(self, instance):
        cur = self._execute(*instance.get_insert_sql())
        self._commit()

        instance._data['id'] = cur.lastrowid


class Table:
    @classmethod
    def _get_name(cls):
        return cls.__name__.lower()

    @classmethod
    def get_create_sql(cls):
        fields = [
            ("id", "INTEGER PRIMARY KEY AUTOINCREMENT")
        ]
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append((name, field.sql_type))
            elif isinstance(field, ForeignKey):
                fields.append((name + "_id", "INTEGER"))

        fields = [" ".join(x) for x in fields]
        return CREATE_TABLE_SQL.format(name=cls._get_name(), fields=", ".join(fields))

    @classmethod
    def get_all_table_sql(cls):
        fields = ['id']
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)
        return SELECT_TABLE_ALL_SQL.format(name=cls._get_name(), fields=', '.join(fields))

    @classmethod
    def get_select_query(cls, **kwargs):
        fields = ['id']
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields.append(name)

        placeholders, params = [], []
        for key, value in kwargs.items():
            placeholders.append(key + ' = ?')
            params.append(value)

        return SELECT_WHERE_SQL.format(
            fields=', '.join(fields),
            name=cls._get_name(),
            query=', '.join(placeholders)
        ), fields, params

    def get_insert_sql(self):
        fields, values, placeholders = [], [], []
        for name, field in inspect.getmembers(self.__class__):
            if isinstance(field, Column):
                fields.append(name)
                values.append(getattr(self, name))
                placeholders.append('?')

        return INSERT_TABLE_SQL.format(name=self._get_name(), fields=", ".join(fields), placeholder=', '.join(placeholders)), values

    def __init__(self, **kwargs):
        self._data = {
            'id': None
        }
        for key, value in kwargs.items():
            self._data[key] = value

    def __getattribute__(self, key):
        # return self._data[key]  This returns an error because it calls itself --> RecursionError

        _data = object.__getattribute__(self, '_data')
        if key in _data:
            return _data[key]

        return object.__getattribute__(self, key)


class Column:
    def __init__(self, type):
        self.type = type

    @property
    def sql_type(self):
        return SQLITE_TYPE_MAP[self.type]


class ForeignKey:
    def __init__(self, table):
        self.table = table


class Author(Table):
    name = Column(str)
    phone_number = Column(int)


class Post(Table):
    title = Column(str)
    body = Column(str)
    author = ForeignKey(Author)
