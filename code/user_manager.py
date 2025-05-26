from database import Database

class UserManager:
    """Handles user authentication and registration with role management."""

    def __init__(self):
        self.db = Database()

    def register_user(self, username, password, role="customer"):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, (username, password, role))
        conn.commit()
        conn.close()

    def authenticate_user(self, username, password):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM users WHERE username=? AND password=?
        """, (username, password))
        user = cursor.fetchone()
        conn.close()
        return user
    