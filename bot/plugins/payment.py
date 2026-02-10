from bot.clients.ton_client import check_payment
from bot.storage.database import connect

def verify_payment(order_id, memo, amount):
    if not check_payment(memo, amount):
        return False
    conn = connect()
    c = conn.cursor()
    c.execute("UPDATE orders SET status='PAID' WHERE id=?", (order_id,))
    conn.commit()
    conn.close()
    return True
