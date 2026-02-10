import sqlite3
from bot.config import DB_PATH

def connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = connect()
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS orders (id TEXT, user_id INT, amount REAL, memo TEXT, status TEXT)")
    conn.commit()
    conn.close()
