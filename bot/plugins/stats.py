import aiosqlite
from config import DB_PATH

async def get_stats():
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("SELECT COUNT(*) FROM orders")
        total = await cur.fetchone()
        return total[0]
