import sqlite3

# Connect to or create a database file
conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)''')

# Insert some data
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

# Commit the changes
conn.commit()

# Query the data
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
