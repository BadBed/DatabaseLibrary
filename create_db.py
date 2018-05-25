import sqlite3
import open_db
import gen_db


def create_tables(cursor):
    cursor.execute('''
CREATE TABLE Book (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  title VARCHAR NOT NULL,
  link VARCHAR
);
''')
    cursor.execute('''
CREATE TABLE Author (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  name VARCHAR NOT NULL,
  surname VARCHAR NOT NULL,
  patronymic VARCHAR
);
''')
    cursor.execute('''
CREATE TABLE Book_Author (
  id_book INTEGER NOT NULL,
  id_author INTEGER NOT NULL,
  PRIMARY KEY (id_author, id_book),
  FOREIGN KEY (id_book) REFERENCES Book(id),
  FOREIGN KEY (id_author) REFERENCES Author(id)
);
''')
    cursor.execute('''
CREATE TABLE BookConfig (
  id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  publisher VARCHAR NOT NULL,
  edition VARCHAR NOT NULL,
  year INTEGER NOT NULL,
  UNIQUE(publisher, edition, year)
);
''')
    cursor.execute('''
CREATE TABLE ConcreteBook (
  id INTEGER PRIMARY KEY NOT NULL UNIQUE,
  id_book INTEGER NOT NULL,
  id_config INTEGER NOT NULL,
  quality VARCHAR NOT NULL DEFAULT "Хорошее",
  is_lost BOOLEAN DEFAULT FALSE,
  FOREIGN KEY (id_book) REFERENCES Book(id),
  FOREIGN KEY (id_config) REFERENCES BookConfig(id)
);
''')
    cursor.execute('''
CREATE TABLE LibClient (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  name VARCHAR NOT NULL,
  surname VARCHAR NOT NULL,
  patronymic VARCHAR,
  priority INTEGER DEFAULT 0
);
''')
    cursor.execute('''
CREATE TABLE Operation (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  id_client INTEGER NOT NULL,
  id_con_book INTEGER NOT NULL,
  take_date DATE NOT NULL,
  return_date DATE,
  FOREIGN KEY (id_client) REFERENCES LibClient(id),
  FOREIGN KEY (id_con_book) REFERENCES ConcreteBook(id)
);
''')
    cursor.execute('''
CREATE TABLE Incident (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  id_client INTEGER NOT NULL,
  id_con_book INTEGER NOT NULL,
  day DATE NOT NULL,
  type VARCHAR NOT NULL,
  description VARCHAR NOT NULL,
  FOREIGN KEY (id_client) REFERENCES LibClient(id),
  FOREIGN KEY (id_con_book) REFERENCES ConcreteBook(id)
); ''')
    cursor.execute('''
CREATE TABLE Student (
  id_client INTEGER PRIMARY KEY NOT NULL UNIQUE,
  faculty VARCHAR NOT NULL,
  specialization VARCHAR NOT NULL,
  sem_num INTEGER NOT NULL,
  FOREIGN KEY (id_client) REFERENCES LibClient(id)
);
''')
    cursor.execute('''
CREATE TABLE FacultyProgram (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  faculty VARCHAR NOT NULL,
  specialization VARCHAR NOT NULL,
  sem_num INTEGER NOT NULL,
  UNIQUE (faculty, specialization, sem_num)
);
''')
    cursor.execute('''
CREATE TABLE Subject (
  id INTEGER PRIMARY KEY NOT NULL UNIQUE,
  title VARCHAR NOT NULL
);
''')
    cursor.execute('''
CREATE TABLE Program_Subject (
  id_subject INTEGER NOT NULL,
  id_program INTEGER NOT NULL,
  PRIMARY KEY (id_subject, id_program),
  FOREIGN KEY (id_subject) REFERENCES Subject(id),
  FOREIGN KEY (id_program) REFERENCES FacultyProgram(id)
);
''')
    cursor.execute('''
CREATE TABLE Book_Subject (
  id_subject INTEGER NOT NULL,
  id_book INTEGER NOT NULL,
  is_necesary BOOLEAN NOT NULL,
  PRIMARY KEY (id_subject, id_book),
  FOREIGN KEY (id_subject) REFERENCES Subject(id),
  FOREIGN KEY (id_book) REFERENCES Book(id)
);
''')


def create_db():
    conn = open_db.open_db()
    cursor = conn.cursor()
    create_tables(cursor)
    conn.commit()
    conn.close()
    gen_db.gen()
