def price(days):
    amount = days * 60
    if days >= 7:
        amount = amount * 0.90   # 10% off
    return amount
