import os
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

bot = Bot(token=os.getenv("8389803915:AAHiPiZDbLdt2JTYL7zOY_vFvF6IKASZ9Bw"))
