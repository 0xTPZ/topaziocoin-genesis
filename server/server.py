import sys
import os
from flask import Flask, jsonify, request
from flask_cors import CORS  # Libera CORS para integração web

# Corrigir o caminho para importar os módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blockchain import blockchain as blockchain_module
from blockchain import transaction as transaction_module

Blockchain = blockchain_module.Blockchain
Transaction = transaction_module.Transaction

# Inicializar Blockchain
blockchain = Blockchain()

# Chave secreta para proteger a mineração
SECRET_KEY = "<REDACTED_HISTORICAL_SECRET>"

# Criar o app Flask
app = Flask(__name__)
CORS(app, origins=["https://topaziocoin.online"])  # <-- Corrigido: CORS só permite esse domínio

# Criar nova transação
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender_address', 'recipient_address', 'amount', 'sender_private_key']
    if not all(k in values for k in required):
        return 'Faltam dados para criar a transação', 400

    transaction = Transaction(
        sender_address=values['sender_address'],
        recipient_address=values['recipient_address'],
        amount=values['amount'],
        sender_private_key=values['sender_private_key']
    )

    blockchain.create_transaction(transaction)

    return jsonify({'message': 'Transação adicionada!'})

# Minerar um novo bloco (proteção com chave secreta)
@app.route('/mine', methods=['POST'])
def mine():
    data = request.get_json()

    miner_address = data.get('miner_address')
    secret_key = data.get('secret_key')

    if not secret_key or secret_key != SECRET_KEY:
        return jsonify({'error': 'Chave secreta inválida.'}), 403

    if not miner_address:
        return 'Endereço do minerador não informado', 400

    blockchain.mine_pending_transactions(miner_address)

    return jsonify({'message': 'Novo bloco minerado!'})

# Ver saldo de um endereço
@app.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    balance = blockchain.get_balance(address)
    return jsonify({'address': address, 'balance': balance})

# Ver a cadeia de blocos completa
@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'transactions': block.transactions,
            'nonce': block.nonce,
            'hash': block.hash,
            'previous_hash': block.previous_hash
        })
    return jsonify({'chain': chain_data, 'length': len(chain_data)})

# Criar nova carteira
@app.route('/wallet/new', methods=['GET'])
def create_wallet():
    new_wallet = blockchain.create_wallet()
    return jsonify({
        'public_key': new_wallet['public_key'],
        'private_key': new_wallet['private_key']
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Porta 5000 para uso com Nginx reverso
