# Snakes Ransomware

Snakes Ransomware is a Python-based tool designed to encrypt and decrypt files within a specified target folder. This program is intended for educational purposes only.

## Table of Contents

- [Installation](#installation)
- [Encryption Process](#encryption-process)
- [Decryption Process](#decryption-process)
- [Disclaimer](#disclaimer)

## Installation

Before running the Snakes Ransomware program, make sure to install the necessary dependencies. You can do this by installing the requirements from the `requirements.txt` file.

```bash
pip3 install -r requirements.txt
```

## Encryption Process

To encrypt the files in a target folder, follow these steps:

1. **Copy the Encryption Script:**
   - Copy the `snakes-encrypt.py` file into the target folder that you want to encrypt.

2. **Run the Script:**
   - Open a terminal and navigate to the target folder.
   - Run the encryption script with the following command:
   
     ```bash
     python3 snakes-encrypt.py
     ```

3. **Encryption Completion:**
   - Once the script has finished running, the files in the target folder will be encrypted.
   - A file named `snakes-key.key` will be created in the same folder. **This key is crucial for decrypting the files, so keep it safe.**

## Decryption Process

If you need to decrypt the files that were previously encrypted, follow these steps:

1. **Copy the Decryption Script:**
   - Copy the `snakes-decrypt.py` file into the target folder that contains the encrypted files.

2. **Add the Encryption Key:**
   - Ensure that the `snakes-key.key` file is in the same folder as the decryption script.

3. **Run the Decryption Script:**
   - Open a terminal, navigate to the target folder, and run the decryption script with the following command:
   
     ```bash
     python3 snakes-decrypt.py
     ```

4. **Decryption Completion:**
   - After running the script, the encrypted files will be decrypted, restoring them to their original state.

## Disclaimer

This software is intended for educational purposes only. The use of ransomware for malicious purposes is illegal and unethical. The author of this software is not responsible for any misuse or damages caused by the use of this program.

---