import uuid
def generate_order(amount):
    return {"id": uuid.uuid4().hex[:8], "memo": "ORD-"+uuid.uuid4().hex[:6], "amount": amount}
