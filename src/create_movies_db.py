import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('movies.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create table 'movies' if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    Title TEXT,
    Year INTEGER,
    Genre TEXT,
    Director TEXT,
    imdbRating REAL
)
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and table created successfully!")
