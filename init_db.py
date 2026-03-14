import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS vouchers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
date TEXT,
days INTEGER,
rate REAL,
daily REAL,
extra REAL,
used REAL,
due REAL,
total_milk REAL,
amount REAL,
final_bill REAL
)
""")

print("Database ready!")

conn.close()