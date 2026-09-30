import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "voicelearn.db"


def create_database():
    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE NOT NULL,
            category TEXT,
            meaning TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_entry(word, category, meaning):
    connection = sqlite3.connect(DB_PATH)

    connection.execute(
        """
        INSERT OR REPLACE INTO entries (word, category, meaning)
        VALUES (?, ?, ?)
        """,
        (word.lower(), category, meaning)
    )

    connection.commit()
    connection.close()


def search_word(word):
    connection = sqlite3.connect(DB_PATH)

    result = connection.execute(
        """
        SELECT word, category, meaning
        FROM entries
        WHERE word = ?
        """,
        (word.lower().strip(),)
    ).fetchone()

    connection.close()

    return result