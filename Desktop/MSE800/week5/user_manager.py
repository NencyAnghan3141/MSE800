from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("User deleted.")


def update_user(user_id, name, email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()
    conn.close()
    print("User updated successfully.")

def add_course(course_name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (name, unit) VALUES (?, ?)", (course_name, unit))
    conn.commit()
    conn.close()
    print(f"Course {course_name} added successfully.")

# Search course by course ID
def search_course_by_id(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
    course = cursor.fetchone()
    conn.close()
    if course:
        print(f"Course found: ID: {course[0]}, Name: {course[1]}, Unit: {course[2]}")
    else:
        print("Course not found.")

def search_course_by_user_name(user_name):
    conn = create_connection()
    cursor = conn.cursor()

    # Assuming user_course relation exists, which isn't yet defined here
    # For now, we're just assuming a search of courses by user name for demonstration
    cursor.execute("""
        SELECT c.name, c.unit FROM courses c
        JOIN users u ON u.name = ?
    """, (user_name,))
    
    courses = cursor.fetchall()
    conn.close()

    if courses:
        print(f"Courses for {user_name}:")
        for course in courses:
            print(f"Course: {course[0]}, Unit: {course[1]}")
    else:
        print("No courses found for this user.")
