import sqlite3


def open_db():
    return sqlite3.connect("lib.db")
