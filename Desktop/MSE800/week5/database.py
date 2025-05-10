import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            unit INTEGER NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

    