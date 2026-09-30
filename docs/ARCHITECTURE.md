# Original architecture

This document describes the recovered implementation as it exists in the public historical edition. Credential values are redacted; application logic is otherwise retained.

## Components

- `blockchain/block.py`: `Block` stores an index, previous hash, timestamp, transactions, nonce, and calculated hash. Its SHA-256 input is direct concatenation of those values, with transaction values converted to strings. There is no canonical serialization or stored-block validation.
- `blockchain/blockchain.py`: `Blockchain` starts with a genesis block whose timestamp is the current time and whose previous hash is the string `"0"`. It holds blocks and pending transactions in process memory. Mining adds a reward transaction of 50 units, searches for a hash with four leading zeroes, appends the block, clears the pending list, and increments difficulty when total chain length (including genesis) is a multiple of ten. The increment is not based on elapsed time.
- `blockchain/transaction.py`: a transaction stores sender, recipient, amount, and a SHA-256 value over the concatenated transaction fields and a supplied private-key string. This is not a public-key digital signature and is not verified by the chain.
- `blockchain/wallet.py`: a random 32-byte hex string is used as a private-key-like value. The “public key” is a SHA-256 hash of that string; the address is `TPZ` plus the first 30 characters of a second SHA-256 hash. There is no asymmetric cryptography or address checksum.
- `server/server.py`: Flask exposes HTTP routes backed by one global in-memory `Blockchain` instance. CORS is restricted in the recovered source to `https://topaziocoin.online`. The mining route compares a submitted value with a hardcoded secret whose value has been redacted from this public copy.
- `notify.py`: a script sends a message to Telegram. Historical token and chat-ID values are redacted; environment variables remain the intended configuration interface in this public copy.

## API routes found in source

| Route | Observed behavior |
| --- | --- |
| `POST /transactions/new` | Reads sender, recipient, amount, and sender private-key fields from JSON; constructs and queues a transaction. It does not check the JSON shape beyond required keys or validate funds/signatures. |
| `POST /mine` | Requires a miner address and the configured secret, then mines pending transactions plus a reward. |
| `GET /balance/<address>` | Sums recorded incoming and outgoing amounts across the in-memory chain. |
| `GET /chain` | Returns the in-memory blocks and their fields. |
| `GET /wallet/new` | Calls `blockchain.create_wallet()`, a method not present in the recovered `Blockchain` class. As written, this route fails. |

## What existed and what did not

**Present in the files:** SHA-256 block hashing; a previous-hash field; a nonce search with a leading-zero target; a genesis block; a fixed mining reward; rudimentary transaction and wallet classes; balance summing; and a Flask API.

**Absent or experimental:** peer-to-peer communication; node discovery; distributed consensus or chain selection; persistent storage; canonical transaction/block encoding; verification of blocks after creation; transaction signature verification; spend authorization; prevention of double-spending; a time-based difficulty adjustment; tested issuance rules; and a working wallet API route. The project is a local process, not a networked blockchain.
