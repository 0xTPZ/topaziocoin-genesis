# Historical security and privacy review

> **HISTORICAL SOFTWARE — NOT FOR PRODUCTION USE**

The prototype is not safe for real funds, private keys, public deployment, or production use. This record distinguishes limitations in the recovered design from the privacy edits made for publication.

## Historical limitations observed

- Transactions are not checked for valid signatures. The stored SHA-256 field is a hash of transaction text plus a supplied key string, not a digital signature.
- The chain does not check balances before accepting transactions, prevent replay or double-spending, validate blocks, or compare competing chains.
- Wallet key derivation is not public-key cryptography. The wallet API route also calls a method absent from the chain class.
- The ledger and pending transactions exist only in process memory and disappear when the process stops.
- The mining reward is fixed at 50. Difficulty starts at four leading zeroes and increases every ten blocks, without timing measurements or an upper bound.
- The Flask development server binds to all interfaces. The transaction route accepts a sender key in request JSON. The mining route used a hardcoded secret. These are unsafe patterns; redacting the historical value does not make the server secure.
- There is no test suite, deployment hardening, persistence layer, or demonstrated P2P/consensus implementation in the recovered files.

These behaviors are documented rather than modernized so that the public edition remains recognizable as historical code.

## Privacy and sanitization

The initial review found these categories of sensitive data, whose actual values are intentionally not reproduced here:

- Database host/name/user/password configuration in `infs.txt`.
- A Telegram bot token and chat ID in `notify.py`.
- A hardcoded mining API secret in `server/server.py`.

The Telegram token, chat ID, and mining secret values were replaced in their original code positions with `<REDACTED_HISTORICAL_SECRET>`. The database credential file is excluded from the public repository. Local run instructions are also excluded as non-implementation material. Python bytecode caches are excluded because they are generated artifacts and may preserve embedded source values. Untouched private originals remain in the local working copy and preservation snapshot; both are Git-ignored and excluded from the public edition.

Treat every credential found during recovery as compromised and rotate/revoke it with its provider. Public documentation does not include secret values. The scan records and source review are summarized in the preservation report; scan patterns are not a guarantee that all possible secrets can be detected automatically.
