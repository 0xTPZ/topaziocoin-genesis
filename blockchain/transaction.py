# blockchain/transaction.py

import hashlib

class Transaction:
    def __init__(self, sender_address, recipient_address, amount, sender_private_key):
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.amount = amount
        self.signature = self.sign_transaction(sender_private_key)

    def sign_transaction(self, private_key):
        tx_string = f"{self.sender_address}{self.recipient_address}{self.amount}"
        signing_string = tx_string + private_key
        return hashlib.sha256(signing_string.encode()).hexdigest()

    def to_dict(self):
        return {
            'sender_address': self.sender_address,
            'recipient_address': self.recipient_address,
            'amount': self.amount,
            'signature': self.signature
        }
