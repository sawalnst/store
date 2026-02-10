from bot.helpers.generator import generate_order
from bot.storage.database import connect

def create_order(user_id, amount):
    order = generate_order(amount)
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO orders VALUES (?, ?, ?, ?, 'WAITING')",
              (order['id'], user_id, amount, order['memo']))
    conn.commit()
    conn.close()
    return order
