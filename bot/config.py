import os
from dotenv import load_dotenv
load_dotenv("/root/store/.env")

BOT_TOKEN = os.getenv("8582890088:AAE6jA8_Hu_HvsAYMyoaQYA2DOY2c-XOsjM")
BOT_NAME = os.getenv("BOT_NAME", "WAllxSTORE")
TON_WALLET = os.getenv("TON_WALLET")
TON_API = "https://tonviewer.com/api"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "storage", "data.db")
