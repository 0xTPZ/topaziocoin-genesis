# blockchain/blockchain.py

from blockchain.block import Block
from blockchain.transaction import Transaction
import time

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.difficulty = 4
        self.mining_reward = 50

    def create_genesis_block(self):
        return Block(0, "0", time.time(), [], 0)

    def get_last_block(self):
        return self.chain[-1]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        reward_tx = Transaction(
            sender_address="MINERAÇÃO",
            recipient_address=miner_address,
            amount=self.mining_reward,
            sender_private_key="MINERAÇÃO"
        )
        self.pending_transactions.append(reward_tx)

        new_block = Block(
            index=self.get_last_block().index + 1,
            previous_hash=self.get_last_block().hash,
            timestamp=time.time(),
            transactions=[tx.to_dict() for tx in self.pending_transactions],
            nonce=0
        )

        nonce = 0
        while True:
            new_block.nonce = nonce
            new_block.hash = new_block.calculate_hash()
            if new_block.hash.startswith('0' * self.difficulty):
                print(f"Bloco minerado: {new_block.hash}")
                self.chain.append(new_block)
                break
            nonce += 1

        self.pending_transactions = []
        self.adjust_difficulty()

    def adjust_difficulty(self):
        if len(self.chain) % 10 == 0 and len(self.chain) > 0:
            self.difficulty += 1
            print(f"Nova dificuldade: {self.difficulty}")

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                tx_data = tx if isinstance(tx, dict) else tx.to_dict()
                if tx_data['sender_address'] == address:
                    balance -= tx_data['amount']
                if tx_data['recipient_address'] == address:
                    balance += tx_data['amount']
        return balance
