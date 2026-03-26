#🛡️ Chunkster: AES-256 Symmetric Encryption Utility tool


## Overview
Chunkster is a Python-based security tool designed to demonstrate robust credential encryption. It bridges the gap between human-readable passwords and machine-strength cryptographic keys.

## 🔐 Cryptographic Implementation

* **Algorithm:** AES-256 (Advanced Encryption Standard).
* **Mode of Operation:** **CBC (Cipher Block Chaining)**. This prevents pattern-matching attacks by ensuring every block of data depends on the previous one.
* **Key Derivation:** Uses **PBKDF2** (Password-Based Key Derivation Function 2) with **100,000 iterations**. 
    * *Why?* This "stretches" the password to make brute-force attacks computationally impossible.
* **Salting:** Every key is unique due to a 16-byte random salt, protecting against "Rainbow Table" attacks.
* **Integrity:** Implements PKCS7 padding to ensure variable-length data fits 16-byte AES blocks.

## 🚀 How to Run
1. Ensure you have the required library:
   `pip install pycryptodome`
2. Run the script:
   `python chunkster.py`

## 📂 Forensic Note
As a Cybersecurity student, I designed this to ensure high entropy in the resulting ciphertext. In a forensic image, this data would appear as randomized noise, providing zero leakage of the original plaintext structure.
