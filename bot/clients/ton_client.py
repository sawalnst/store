import requests
from bot.config import TON_API, TON_WALLET

def check_payment(memo, amount):
    url = f"{TON_API}/accounts/{TON_WALLET}/transactions"
    r = requests.get(url).json()
    for tx in r.get("transactions", []):
        if memo in str(tx):
            return True
    return False
