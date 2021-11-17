
import os
import sqlite3
import pytest
from orm import Database, Table, Column, ForeignKey


@pytest.fixture()
def create_table():
    class Author(Table):
        name = Column(str)
        lucky_number = Column(int)

    class Post(Table):
        title = Column(str)
        body = Column(str)
        author = ForeignKey(Author)

    return Post, Author


@pytest.fixture(scope='function')
def create_file():
    path = 'test_orm.sqlite'
    yield path

    os.unlink(path)


class TestDatabase:
    def test_create_file(self, create_file):
        global db

        db = Database(create_file)
        assert os.path.isfile(create_file)

    def test_file_connection(self, create_file, create_table):
        global post, author

        self.test_create_file(create_file)
        assert isinstance(db.conn, sqlite3.Connection)

        assert db.tables == []

        post, author = create_table

        db.create(post)
        assert ('post',) in db.tables

        db.create(author)
        assert ('author',) in db.tables


class TestTableInformation(TestDatabase):
    def test_table_name(self, create_file, create_table):
        super().test_file_connection(create_file, create_table)

        assert post._get_name() == 'post'
        assert author._get_name() == 'author'

    def test_foreign_key(self, create_file, create_table):
        self.test_table_name(create_file, create_table)
        assert 'author_id' in post.get_create_sql()


class TestCreatedTable(TestDatabase):
    def test_create_author_instance(self, create_file, create_table):
        global vince

        super().test_file_connection(create_file, create_table)
        vince = author(name="Vincent", lucky_number=13)

        assert vince.name == "Vincent"
        assert vince.id is None
        assert vince.lucky_number == 13

    def test_create_save_author_instance(self, create_file, create_table):
        self.test_create_author_instance(create_file, create_table)

        assert vince.id is None
        db.save(vince)

        assert vince.id == 1

    def test_create_more_author(self, create_file, create_table):
        self.test_create_save_author_instance(create_file, create_table)

        samad = author(name="Samad", lucky_number=56)
        db.save(samad)
        assert samad.id == 2

        kunle = author(name="Kunle", lucky_number=28)
        db.save(kunle)
        assert kunle.id == 3

        ayo = author(name="Ayomide", lucky_number=22)
        db.save(ayo)
        assert ayo.id == 4


class TestAllDatabaseEntry(TestCreatedTable):
    def test_query_all_author(self, create_file, create_table):
        super().test_create_more_author(create_file, create_table)

        assert author.get_all_table_sql() == "SELECT id, lucky_number, name FROM author;"
        assert len(db.all(author)) == 4
        assert (2, 56, 'Samad') in db.all(author)

    def test_query_certain_author(self, create_file, create_table):
        super().test_create_more_author(create_file, create_table)

        ayo = db.get(author, 4)
        assert author.get_select_query(id=4) == (
            "SELECT id, lucky_number, name FROM author WHERE id = ?;",
            ['id', 'lucky_number', 'name'],
            [4],
        )
        assert ayo.name == "Ayomide"


class TestColumn:
    def test_column(self):
        for key, value in [(int, "INTEGER"), (float, "REAL")]:
            field = Column(key)
            assert field.sql_type == value
