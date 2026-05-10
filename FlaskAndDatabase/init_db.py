from database import get_db_connection

conn = get_db_connection()
conn.execute('''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                course TEXT NOT NULL
            )''')
conn.commit()
conn.close()

print("Database initialized and students table created successfully.")
