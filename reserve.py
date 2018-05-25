STUDENT_NEEDED_BOOKS = """
SELECT b.id, b.title, COUNT(DISTINCT stud.id_client)
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
GROUP BY b.id;
""" # no Args