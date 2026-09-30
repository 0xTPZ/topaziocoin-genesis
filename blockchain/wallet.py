# blockchain/wallet.py

import hashlib
import secrets

class Wallet:
    def __init__(self):
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()
        self.address = self.generate_address()

    def generate_private_key(self):
        return secrets.token_hex(32)

    def generate_public_key(self):
        return hashlib.sha256(self.private_key.encode()).hexdigest()

    def generate_address(self):
        public_key_hash = hashlib.sha256(self.public_key.encode()).hexdigest()
        return "TPZ" + public_key_hash[:30]  # Endereço estilo TopazioCoin
