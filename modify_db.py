import sqlite3
import open_db

ADD_CLIENT = '''
INSERT INTO LibClient (id, name, surname, patronymic)
VALUES (?, ?, ?, ?);
'''

ADD_STUDENT = '''
INSERT INTO Student (id_client, faculty, specialization, sem_num)
VALUES (?, ?, ?, ?);
'''

DEL_STUDENT = '''
DELETE FROM Student
WHERE id_client = ?;
'''

ADD_BOOK = '''
INSERT INTO Book (id, title, link)
VALUES (?, ?, ?);
'''


def add_client(conn, id=None, name=None, surname=None, patronymic=None):
    cursor = conn.cursor()
    cursor.execute(ADD_CLIENT, (id, name, surname, patronymic))
    conn.commit()


def make_student(conn, id=None, faculty=None, spec=None, sem_num=1):
    cursor = conn.cursor()
    cursor.execute(ADD_STUDENT, (id, faculty, spec, sem_num))
    conn.commit()


def make_non_student(conn, id=None):
    cursor = conn.cursor()
    cursor.execute(DEL_STUDENT, (id))
    conn.commit()


def add_student(conn, id=None, name=None, surname=None, patronymic=None,
                faculty=None, spec=None, sem_num=1):
    add_client(conn, id, name, surname, patronymic)
    make_student(conn, id, faculty, spec, sem_num)


