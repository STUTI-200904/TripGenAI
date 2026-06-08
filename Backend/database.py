import sqlite3

conn = sqlite3.connect("tripgenai.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS trips(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination TEXT,
    days INTEGER,
    budget INTEGER,
    travel_type TEXT,
    interests TEXT
)
""")

conn.commit()