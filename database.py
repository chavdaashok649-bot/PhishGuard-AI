import sqlite3

DB_NAME = "phishing.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        result TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()


def add_scan(url, result, score):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO history(url,result,score) VALUES(?,?,?)",
        (url, result, score)
    )

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT url,result,score
    FROM history
    ORDER BY id DESC
    """)

    rows = cur.fetchall()

    conn.close()

    history = []

    for row in rows:

        history.append({
            "url": row[0],
            "result": row[1],
            "score": row[2]
        })

    return history


def get_counts():

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM history")
    total = cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM history
    WHERE result LIKE '%Safe%'
    """)
    safe = cur.fetchone()[0]

    cur.execute("""
    SELECT COUNT(*)
    FROM history
    WHERE result LIKE '%Phishing%'
    """)
    phishing = cur.fetchone()[0]

    conn.close()

    return total, safe, phishing