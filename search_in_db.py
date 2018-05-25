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
SELECT Book.id, Book.title, Book_Subject.is_necesary, Author.surname, Author.name,
  Author.patronymic
FROM FacultyProgram
JOIN Program_Subject
ON FacultyProgram.id = Program_Subject.id_program
JOIN Subject
ON Subject.id = Program_Subject.id_subject
JOIN Book_Subject
ON Subject.id = Book_Subject.id_subject
JOIN Book
ON Book.id = Book_Subject.id_book
JOIN Book_Author
ON Book.id = Book_Author.id_book
JOIN Author
ON Author.id = Book_Author.id_author
WHERE FacultyProgram.faculty = ?
AND FacultyProgram.specialization = ?
AND FacultyProgram.sem_num = ?;
''' # Args - faculty +

INCIDENT_BY_USER = '''
SELECT Incident.type, Incident.day, Incident.description
FROM Incident
JOIN LibClient
ON Incident.id_client = LibClient.id
WHERE LibClient.id = ?;
''' # Args - user id

BOOKS_FOR_FIX = """
SELECT title, count(Book.id) FROM Book
JOIN ConcreteBook as cb ON Book.id = cb.id_book
WHERE quality != 'Хорошее' AND is_lost = 0
GROUP BY title;
""" # no Args

LOST_BOOKS = """
SELECT title, count(Book.id) FROM Book
JOIN ConcreteBook as cb ON Book.id = cb.id_book
WHERE is_lost = 1
GROUP BY title;
""" # no Args


BOOKS_WITH_CONFIGS = """
SELECT title, publisher, edition, year, COUNT(cb.id) as amount 
FROM Book
JOIN ConcreteBook AS cb ON Book.id = cb.id_book
JOIN BookConfig AS bc ON bc.id = cb.id_config
where quality = 'Хорошее' AND is_lost = 0
GROUP BY title, bc.id
ORDER BY title, year;
""" # no Args

STUDENT_NEEDED_BOOKS = """
SELECT b.id, b.title, 
COUNT(DISTINCT stud.id_client) OVER (PARTITION BY Book.id)
FROM Book AS b
JOIN Book_Subject AS bs
ON b.id = bs.id_book
JOIN Subject AS s
ON s.id = bs.id_subject
JOIN Program_Subject AS ps
ON ps.id_program = s.id
JOIN FacultyProgram AS p
ON p.id = ps.id_program
JOIN Student AS stud
ON stud.faculty = p.faculty
AND stud.specialization = p.specialization
AND stud.sem_num = p.sem_num
""" # no Args

BOOKS_FOR_STUDENT = """
SELECT DISTINCT Book.id, Book.title
FROM Book
JOIN Book_Subject AS bs ON bs.id_book = Book.id
JOIN Subject AS s ON s.id = bs.id_subject
JOIN Program_Subject AS ps ON ps.id_subject = s.id
JOIN FacultyProgram AS p ON p.id = ps.id_program
JOIN Student AS st ON st.faculty = p.faculty 
AND st.specialization = p.specialization 
AND st.sem_num = p.sem_num
WHERE st.id_client = ? AND bs.is_necesary = 1

EXCEPT

SELECT Book.title, ConcreteBook.id
FROM LibClient
JOIN Operation
ON Operation.id_client = LibClient.id
JOIN ConcreteBook
ON Operation.id_con_book = ConcreteBook.id
JOIN Book
ON Book.id = ConcreteBook.id_book
WHERE LibClient.id = ?
AND Operation.return_date IS NULL;
"""




def query(conn, q, args):
    cursor = conn.cursor()
    cursor.execute(q, args)
    return cursor.fetchall()
