import asyncio
from clients.telegram_client import bot
from storage import init_db

async def main():
    init_db()
    print("Bot started")
    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
