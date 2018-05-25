import random
import datetime
from open_db import open_db
import modify_db
from for_gen import *
from random import randint


def rand_date(fyear):
    return datetime.date(randint(fyear, 2017), randint(1, 12), randint(1, 28))


def gen_books(cursor):
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Курс математического анализа',
                'https://lib.mipt.ru/books/fsdfnksdjn')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Сборник задач по математическому анализу. Часть 1', 
                'https://lib.mipt.ru/books/sjdnaskaksj')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Сборник задач по математическому анализу. Часть 2', 
                'https://lib.mipt.ru/books/afsvxbasjhnx')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Сборник задач по математическому анализу. Часть 3', 
                'https://lib.mipt.ru/books/qwertasbsa')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Курс аналитической геометрии и линейной алгебры',
                'https://lib.mipt.ru/books/ncdwhvdfj')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Алгоритмы. Построение и анализ',
                 'https://lib.mipt.ru/books/ahbsasjhbx')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Заметки о женской логике', 
                'https://lib.mipt.ru/books/hxgcbhj')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Квантовая механика.', 
                'https://lib.mipt.ru/books/hsdgcbhksa')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Сборник задач по общей физике',
                'https://lib.mipt.ru/books/kshdcbasj')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Алгоритмы обнаружения эмпирических закономерностей', 
                'https://lib.mipt.ru/books/fhxbzghzuxh')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Разработка требований к программному обеспечению',
                'https://lib.mipt.ru/books/jdfvbfjvbdfjd')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Лабораторные работы по общей физике',
                'https://lib.mipt.ru/books/gydcvsjcbdj')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Неорганическая химия', 'https://lib.mipt.ru/books/jxzcbzzxxhc')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Приключения домовенка Кузи',
                'https://lib.mipt.ru/books/jhxbczjxcxcj')""")
    cursor.execute("""INSERT INTO Book(title, link) VALUES
                ('Design Patterns', 'https://lib.mipt.ru/books/dskjfvbhdsfj')""")
    return 15


def gen_configs(cursor):
    eds = ['1-е стереотипное', '2-е дополненное', '3-е переработанное']
    pubs = ['Росмен', 'Махаон', 'Просвещение', 'ФизМатЛиб', 'Интеллект']
    for i in range(len(eds)):
        for j in range(len(pubs)):
            year = 1960 + (i + 1)**3 + 5*j
            cursor.execute("""INSERT INTO BookConfig(publisher, edition, year)
                              VALUES (?, ?, ?)""", (eds[i], pubs[j], year))
    return len(eds)*len(pubs)


def gen_con_books(cursor, nb, nc):
    n = 1000
    for i in range(n):
        x = random.randint(1, nb)
        y = random.randint(1, nc)
        cursor.execute("""INSERT INTO ConcreteBook(id_book, id_config)
                          VALUES (?, ?)""", (x, y))

    for i in range(30):
        x = random.randint(1, n)
        cursor.execute("""UPDATE ConcreteBook SET quality = 'Исписана' 
                WHERE id = ?""", (x,))

    for i in range(20):
        x = random.randint(1, n)
        cursor.execute("""UPDATE ConcreteBook SET quality = 'Порвана' 
                WHERE id = ?""", (x,))

    for i in range(30):
        x = random.randint(1, n)
        cursor.execute("""UPDATE ConcreteBook SET is_lost = ? 
                WHERE id = ?""", (True, x))

    return n


def randof(lst):
    i = random.randint(0, len(lst)-1)
    return lst[i]


def gen_clients(cursor):
    st = set()
    n = 200
    for i in range(n):
        while True:
            is_tyan = (random.randint(1, 4) == 2)
            if is_tyan:
                a, b, c = randof(JNAMES), randof(JSURS), randof(JPATS)
            else:
                a, b, c = randof(MNAMES), randof(MSURS), randof(MPATS)
            if (a, b, c) not in st:
                cursor.execute("""INSERT INTO LibClient(name, surname, patronymic)
                                  VALUES (?, ?, ?)""", (a, b, c))
                st.add((a, b, c))
                break

    for i in range(20):
        x = random.randint(1, n)
        cursor.execute("""UPDATE LibClient SET priority = 1 
                WHERE id = ?""", (x,))

    for i in range(3):
        x = random.randint(1, n)
        cursor.execute("""UPDATE LibClient SET priority = 2 
                WHERE id = ?""", (x,))

    return n


def gen_authors(cursor):
    st = set()
    n = 30
    for i in range(n):
        while True:
            is_tyan = (random.randint(1, 4) == 2)
            if is_tyan:
                a, b, c = randof(JNAMES), randof(JSURS), randof(JPATS)
            else:
                a, b, c = randof(MNAMES), randof(MSURS), randof(MPATS)
            if (a, b, c) not in st:
                cursor.execute("""INSERT INTO Author(name, surname, patronymic)
                                  VALUES (?, ?, ?)""", (a, b, c))
                st.add((a, b, c))
                break
    return n


def gen_author_book(cursor, na, nb):
    st = set()
    n = 80
    for i in range(n):
        while True:
            x = random.randint(1, na)
            y = random.randint(1, nb)
            if (x, y) not in st:
                cursor.execute("""INSERT INTO Book_Author(id_author, id_book)
                                  VALUES (?, ?)""", (x, y))
                st.add((x, y))
                break
    return n


def gen_incidents(cursor, nu, nb):
    n1 = 20
    n2 = 10

    for i in range(n1):
        x = random.randint(1, nu)
        y = random.randint(1, nb)
        date = rand_date(1990)
        type = 'Порча книги'
        if randint(1, 2) == 1:
            descr = 'Некоторые страницы книги были порваны'
        else:
            descr = 'Некоторые страницы книги были исписаны'
        cursor.execute("INSERT INTO Incident (id_client, id_con_book, type, day, "
                       "description) VALUES (?, ?, ?, ?, ?)", (x, y, type, date, descr))

    for i in range(n2):
        x = random.randint(1, nu)
        y = random.randint(1, nb)
        date = datetime.date(randint(1960, 2017), randint(1, 12), randint(1, 28))
        type = 'Потеря книги'
        descr = 'Книга была потеряна'

        cursor.execute("INSERT INTO Incident (id_client, id_con_book, type, day, "
                       "description) VALUES (?, ?, ?, ?, ?)", (x, y, type, date, descr))

    return n1 + n2


def gen_students(cursor, nu):
    res = 0
    for i in range(1, nu + 1):
        if randint(1, 5) != 3:
            res += 1
            dir = randof(STUDIES)
            sem = randint(1, 8)
            cursor.execute(modify_db.ADD_STUDENT, (i, dir[0], dir[1], sem))
    return res


def gen_operations(cursor, nu, nb):
    res = 0
    for i in range(1, nb + 1):
        sz = randint(0, 7)

        days = [rand_date(2000) for j in range(sz)]
        days.sort()
        if len(days) % 2 == 1:
            days.append(None)

        for j in range(len(days)//2):
            res += 1
            cursor.execute("""INSERT INTO Operation (id_client, id_con_book, take_date, 
                    return_date) VALUES (?, ?, ?, ?)""", (randint(1, nu), i,
                                    days[2*j], days[2*j + 1]))
    return res


def gen_program(cursor):
    res = 0
    for i in range(1, 9):
        for d in STUDIES:
            res += 1
            cursor.execute("""INSERT INTO FacultyProgram(faculty, specialization, 
                              sem_num) VALUES (?, ?, ?)""", (d[0], d[1], i))
    return res


def gen_subjects(cursor):
    cursor.execute("INSERT INTO Subject(title) VALUES ('Введение в матанализ')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Аналитическая геометрия')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Линейная алгебра')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Введение впрограммиорвание')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Алгоритмы и структуры данных')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Базы данных')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Неорганическая химия')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Общая физика: механика')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Общая физика: оптика')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Общая физика: термодинамика')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Аналитическая механика')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Машинное обучение')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Гармонический анализ')")
    cursor.execute("INSERT INTO Subject(title) VALUES ('Математическая логика')")
    return 14


def gen_program_subject(cursor, np, ns):
    st = set()
    n = 150
    for i in range(n):
        while True:
            x = random.randint(1, np)
            y = random.randint(1, ns)
            if (x, y) not in st:
                cursor.execute("""INSERT INTO Program_Subject(id_program, id_subject)
                                      VALUES (?, ?)""", (x, y))
                st.add((x, y))
                break
    return n


def gen_book_subject(cursor, nb, ns):
    st = set()
    n1 = 50
    n2 = 100
    for i in range(n1):
        while True:
            x = random.randint(1, nb)
            y = random.randint(1, ns)
            if (x, y) not in st:
                cursor.execute("""INSERT INTO Book_Subject(id_book, id_subject, 
                        is_necesary) VALUES (?, ?, 1)""", (x, y))
                st.add((x, y))
                break

    for i in range(n2):
        while True:
            x = random.randint(1, nb)
            y = random.randint(1, ns)
            if (x, y) not in st:
                cursor.execute("""INSERT INTO Book_Subject(id_book, id_subject, 
                        is_necesary) VALUES (?, ?, 0 )""", (x, y))
                st.add((x, y))
                break

    return n1 + n2


def gen():
    conn = open_db()
    cursor = conn.cursor()

    nbook = gen_books(cursor)
    nconfig = gen_configs(cursor)
    nconc = gen_con_books(cursor, nbook, nconfig)
    nuser = gen_clients(cursor)
    nath = gen_authors(cursor)
    gen_author_book(cursor, nath, nbook)
    gen_incidents(cursor, nuser, nconc)
    gen_operations(cursor, nuser, nconc)
    gen_students(cursor, nuser)
    nprog = gen_program(cursor)
    nsubj = gen_subjects(cursor)
    gen_program_subject(cursor, nprog, nsubj)
    gen_book_subject(cursor, nbook, nsubj)

    conn.commit()
