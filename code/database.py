import sqlite3

class Database:
    """Database connection and schema initialization for car rental system."""

    def __init__(self, db_name="car_rental.db"):
        self.db_name = db_name
        self.initialize_schema()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def initialize_schema(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                role TEXT
            )
        """)

        # Cars table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                id TEXT PRIMARY KEY,
                make TEXT,
                model TEXT,
                year INTEGER,
                mileage INTEGER,
                min_rent_days INTEGER,
                max_rent_days INTEGER,
                available INTEGER
            )
        """)

        # Bookings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                car_id TEXT,
                start_date TEXT,
                end_date TEXT,
                status TEXT,
                fee REAL,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(car_id) REFERENCES cars(id)
            )
        """)

        conn.commit()
        conn.close()
