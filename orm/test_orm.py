
import sqlite3
import pytest
import shutil
from orm import Database, Table, Column, ForeignKey
from pathlib import Path


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


@pytest.fixture()
def create_file(tmp_path):
    path = tmp_path / 'test.db'
    yield path

    shutil.rmtree(tmp_path)


class TestDatabase:

    def test_create_file(self, create_file):
        assert isinstance(create_file, Path)

    def test_file(self, create_file, create_table):
        global db

        db = Database(create_file)
        assert isinstance(db.conn, sqlite3.Connection)

        assert db.tables == []

        post, author = create_table

        db.create(post)
        assert ('post', ) in db.tables

        db.create(author)
        assert ('author', ) in db.tables


class TestCreatedTable(TestDatabase):
    def test_table_name(self, create_table):
        post, author = create_table
        assert post._get_name() == 'post'
        assert author._get_name() == 'author'

    def test_foreign_key(self, create_table):
        post, _ = create_table
        assert 'author_id' in post.get_create_sql()

    def test_create_author_instance(self, create_table):
        global vince

        _, author = create_table
        vince = author(name="Vincent", lucky_number=13)

        assert vince.name == "Vincent"
        assert vince.id is None
        assert vince.lucky_number == 13


class TestColumn:
    def test_column(self):
        for key, value in [(int, "INTEGER"), (float, "REAL")]:
            field = Column(key)
            assert field.sql_type == value
