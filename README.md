# TopazioCoin Genesis

## The First Topazio Blockchain Prototype

> **HISTORICAL SOFTWARE — NOT FOR PRODUCTION USE**

TopazioCoin Genesis is a preserved early blockchain experiment. It is a small Python prototype, not a production cryptocurrency or a current implementation of Topazio Network. It must not be used to store value, manage real keys, or provide security for a network. It does not represent the security, architecture, or capabilities of the modern Topazio Network.

The original design and limitations are preserved for historical study. Private configuration and exposed credentials found in the recovered files were excluded or redacted in this public edition. See [the historical security notes](docs/SECURITY-HISTORICAL.md) before inspecting or running the code.

## What the prototype contains

- A `Block` that hashes its index, previous hash, timestamp, transaction text, and nonce with SHA-256.
- A `Blockchain` that creates a time-dependent genesis block, mines by searching for a hash with a fixed number of leading zeroes, and calculates balances by summing recorded amounts.
- A simple `Transaction` representation and a `Wallet` that derives a demonstration address from hashes.
- A Flask API with routes for transactions, mining, balances, the in-memory chain, and wallet creation.
- A separate Telegram notification script, with its historical credential values redacted.

This is a single-process, in-memory experiment. It has no peer-to-peer network, persistent ledger, consensus between nodes, transaction validation, or cryptographic signature verification. Some API behavior does not work as its route names suggest. These details are recorded in [the architecture notes](docs/ARCHITECTURE.md).

## Historical context

I began thinking more deeply about blockchain, cryptocurrencies, and the idea of Topazio while I was going through a period of depression. I was still learning, and this implementation was very simple compared with what the idea would later become. Even so, the code represented a much larger dream than I could build at the time. Creating projects, imagining possibilities, and developing the idea of Topazio were part of that period of my life.

Years later, recovering this code let me recognize ideas that would eventually evolve into Topazio Network. At the time, I did not know how far the idea might go. This is a personal account of the context in which I created projects; it does not claim that programming or Topazio cured depression.

## Dates and preservation

The available source-file modification timestamps fall between **27 and 29 April 2025**. There is no Git history or dated project documentation in the recovered directory, so these filesystem timestamps are evidence of when the files were last modified, not independently verified proof of their original creation. The project was recovered and prepared for historical publication by **30 September 2026**; that is the publication date, not an original development date. See [the timeline](docs/TIMELINE.md) and [the original-state record](docs/ORIGINAL-STATE.md) for the evidence and its limits.

## Layout

```text
blockchain/
  block.py
  blockchain.py
  transaction.py
  wallet.py
server/
  server.py
notify.py
docs/
```

The original database credential file (`infs.txt`), local run instructions (`server/inf.txt`), and Python bytecode caches are kept out of the public edition. An untouched local preservation copy is also excluded from Git. See [the preservation record](docs/ORIGINAL-STATE.md).

## License

No license is included because the recovered material did not establish licensing terms or rights-holder details. All rights remain with their respective rights holders. Contact the author for permission to reuse the code.
