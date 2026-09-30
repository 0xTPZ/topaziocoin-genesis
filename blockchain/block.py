# blockchain/block.py

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transactions_string = ''.join(str(tx) for tx in self.transactions)
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{transactions_string}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()
