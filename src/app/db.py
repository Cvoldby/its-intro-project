import os
import sqlite3
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_PATH = Path(os.getenv("DB_PATH", "data/my_project.db"))


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()
