import sqlite3

def init_db():
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        score REAL,
        similarity REAL
    )
    """)

    conn.commit()
    conn.close()


def save_result(filename, score, similarity):
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO results (filename, score, similarity) VALUES (?, ?, ?)",
        (filename, score, similarity)
    )

    conn.commit()
    conn.close()