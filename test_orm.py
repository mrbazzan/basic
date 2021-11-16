
import sqlite3
import pytest
import shutil
from orm import Database, Table, Column, ForeignKey
from pathlib import Path


class Post(Table):
    title = Column(str)
    body = Column(str)


class Author(Table):
    name = Column(str)
    phone_number = Column(int)
    post = ForeignKey(Post)


@pytest.fixture()
def create_file(tmp_path):
    path = tmp_path / 'test.db'
    yield path

    shutil.rmtree(tmp_path)


class TestDatabase:

    def test_create_file(self, create_file):
        assert isinstance(create_file, Path)

    def test_file(self, create_file):
        path = Database(create_file)
        assert isinstance(path.conn, sqlite3.Connection)

    def test_creation(self, create_file):
        path = Database(create_file)
        assert path.tables == []

        path.create(Post)
        assert ('post', ) in path.tables

        path.create(Author)
        assert ('author', ) in path.tables


class TestCreatedTable:
    def test_table_name(self):
        assert Post._get_name() == 'post'
        assert Author._get_name() == 'author'

    def test_foreign_key(self):
        assert 'post_id' in Author.get_create_sql()


class TestColumn:
    def test_column(self):
        for key, value in [(int, "INTEGER"), (float, "REAL")]:
            field = Column(key)
            assert field.sql_type == value
