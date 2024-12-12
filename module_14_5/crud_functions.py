import sqlite3


def initiate_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products(
                id INT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INT NOT NULL)'''
              )
    c.execute('''CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INT NOT NULL,
                balance INT NOT NULL)'''
              )
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    all_products = []
    req = c.execute('SELECT * FROM Products').fetchall()
    for row in req:
        all_products.append(row)
    return all_products


def write_product():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    for i in range(1, 5):
        c.execute('INSERT INTO Products VALUES(?, ?, ?, ?)', (f'{i}', f'Продукт {i}', f'Описание {i}', f'{i * 100}'))
        conn.commit()
        conn.close()
        return True


def is_included(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    req = c.execute('SELECT * FROM Users').fetchall()
    for row in req:
        if row[1] == username:
            return True
    return False


def add_user(username, email, age):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    if not is_included(username):
        c.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)', (f'{username}', f'{email}', f'{age}', 1000))
    else:
        print('Такой пользователь уже существует')
    conn.commit()
    conn.close()
    return True
