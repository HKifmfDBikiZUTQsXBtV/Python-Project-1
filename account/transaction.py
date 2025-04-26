from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"""
Time of transaction: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
Type of transaction: {self.transaction_type.upper()}
Amount exchanged in transaction: {self.amount}"""
