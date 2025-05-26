import uuid
from datetime import datetime
from database import Database

class BookingService:
    """Handles rental bookings, approvals, rejections, and fee calculations."""

    def __init__(self):
        self.db = Database()

    def create_booking(self, user_id, car_id, start_date, end_date):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        # Check car availability and rental duration limits
        cursor.execute("SELECT min_rent_days, max_rent_days FROM cars WHERE id=? AND available=1", (car_id,))
        car = cursor.fetchone()
        if not car:
            print("Car not available or does not exist.")
            return

        min_days, max_days = car
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            rental_days = (end - start).days
        except ValueError:
            print("Invalid date format.")
            return

        if rental_days < min_days or rental_days > max_days or rental_days <= 0:
            print(f"Rental period must be between {min_days} and {max_days} days.")
            return

        # Fee calculation (basic rate + weekend multiplier for demo)
        base_rate = 50
        weekend_surcharge = 10
        fee = rental_days * base_rate
        if start.weekday() in (5, 6) or end.weekday() in (5, 6):  # If start or end on weekend
            fee += weekend_surcharge

        booking_id = str(uuid.uuid4())[:8]
        cursor.execute("""
            INSERT INTO bookings (id, user_id, car_id, start_date, end_date, status, fee)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (booking_id, user_id, car_id, start_date, end_date, "Pending", fee))
        conn.commit()
        conn.close()
        return booking_id

    def approve_booking(self, booking_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE bookings SET status='Approved' WHERE id=?", (booking_id,))
        cursor.execute("""
            UPDATE cars SET available=0
            WHERE id=(SELECT car_id FROM bookings WHERE id=?)
        """, (booking_id,))
        conn.commit()
        conn.close()

    def get_user_bookings(self, user_id):
        """Returns all bookings and fees for a given user."""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, car_id, start_date, end_date, status, fee
            FROM bookings
            WHERE user_id=?
             """, (user_id,))
        bookings = cursor.fetchall()
        conn.close()
        return bookings


    def reject_booking(self, booking_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE bookings SET status='Rejected' WHERE id=?", (booking_id,))
        conn.commit()
        conn.close()
