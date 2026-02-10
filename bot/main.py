import asyncio
from aiogram import Dispatcher, types
from aiogram.filters import Command
from bot.clients.telegram_client import bot
from bot.storage.database import init_db
from bot.plugins.order import create_order
from bot.plugins.payment import verify_payment
from bot.plugins.processor import process_order
from bot.config import TON_WALLET

dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("Welcome to Store Bot\nUse /order")

@dp.message(Command("order"))
async def order(msg: types.Message):
    order = create_order(msg.from_user.id, 1.5)
    await msg.answer(
        f"Send {order['amount']} TON to:\n{TON_WALLET}\nMemo: {order['memo']}\n/cek {order['id']}"
    )

@dp.message(Command("cek"))
async def cek(msg: types.Message):
    oid = msg.text.split()[1]
    if verify_payment(oid, "", 1.5):
        await msg.answer(process_order(oid))
    else:
        await msg.answer("Payment not found")

async def main():
    init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
