import uuid
from database import Database

class CarInventory:
    """Handles car-related operations for admins and customer viewing."""

    def __init__(self):
        self.db = Database()

    def add_new_car(self, make, model, year, mileage, min_days, max_days):
        car_id = str(uuid.uuid4())[:8]
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cars (id, make, model, year, mileage, min_rent_days, max_rent_days, available)
            VALUES (?, ?, ?, ?, ?, ?, ?, 1)
        """, (car_id, make, model, year, mileage, min_days, max_days))
        conn.commit()
        conn.close()
        return car_id

    def get_available_cars(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars WHERE available=1")
        cars = cursor.fetchall()
        conn.close()
        return cars

    def update_car(self, car_id, make, model, year, mileage, min_days, max_days):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE cars
            SET make=?, model=?, year=?, mileage=?, min_rent_days=?, max_rent_days=?
            WHERE id=?
        """, (make, model, year, mileage, min_days, max_days, car_id))
        conn.commit()
        conn.close()

    def delete_car(self, car_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cars WHERE id=?", (car_id,))
        conn.commit()
        conn.close()
