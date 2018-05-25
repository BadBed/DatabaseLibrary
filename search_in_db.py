import sqlite3

BOOKS_BY_AUTHOR = '''
SELECT Book.id, Book.title
FROM Book
JOIN Book_Author
ON Book.id = Book_Author.id_book
JOIN Author
ON Book_Author.id_author = Author.id
WHERE Author.name = ?
AND Author.surname = ?
AND Author.patronymic = ?;
''' # Args - NSP +

DEBTS = '''
SELECT Book.title, ConcreteBook.id
FROM LibClient
JOIN Operation
ON Operation.id_client = LibClient.id
JOIN ConcreteBook
ON Operation.id_con_book = ConcreteBook.id
JOIN Book
ON Book.id = ConcreteBook.id_book
WHERE LibClient.id = ?
AND Operation.return_date IS NULL
''' # Args - id +

BOOKS_FOR_PROGRAM = '''
SELECT Book.id, Book.title
FROM FacultyProgram
JOIN Program_Subject
ON FacultyProgram.id = Program_Subject.id_program
JOIN Subject
ON Subject.id = Program_Subject.id_subject
JOIN Book_Subject
ON Subject.id = Book_Subject.id_subject
JOIN Book
ON Book.id = Book_Subject.id_book
WHERE FacultyProgram.faculty = ?;
''' # Args - faculty

INCIDENT_BY_USER = '''
SELECT Incident.type, Incident.day, Incident.description
FROM Incident
JOIN LibClient
ON Incident.id_client = LibClient.id
WHERE LibClient.id = ?;
''' # Args - user id

COUNT_GOOD_CONCRETE_BOOKS = None

BOOKS_FOR_FIX = None

BOOKS_FOR_STUDENT = None





def query(conn, q, args):
    cursor = conn.cursor()
    cursor.execute(q, args)
    return cursor.fetchall()
