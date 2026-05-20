import sqlite3
from datetime import datetime

DB_NAME = "submission_history.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            row_number INTEGER,
            record_data TEXT,
            status TEXT,
            message TEXT,
            submitted_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_history(row_number, record_data, status, message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history 
        (row_number, record_data, status, message, submitted_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        row_number,
        str(record_data),
        status,
        message,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows