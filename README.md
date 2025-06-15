# Command Logger

A secure and interactive CLI-based command logging tool built in Python. It is designed for military-style or mission-critical operations where reliable command tracking, encryption, and audit logs are essential.

## Features

- Accepts and logs system or custom terminal commands
- Structured JSON log storage with timestamps and usernames
- Real-time system command execution using `subprocess`
- Custom commands like `run` and `halt` for simulation
- Optional encryption/decryption of logs using `cryptography`
- Tracks user command history in a separate file
- Interactive CLI interface styled with `Rich` and built using `Typer`
- Modular code structure for easy maintenance

## Technologies Used

- Python 3.11+
- Typer
- Rich
- Cryptography

## Project Structure

Command Logger/
├── logger/
│ ├── init.py
│ ├── encryptor.py
│ ├── log_writer.py
│ ├── utils.py
├── logs/
│ ├── command_log.json
│ ├── secret.key
├── tests/
│ ├── test_log_writer.py
├── venv/
├── main.py
├── history.txt
├── .env
├── .gitignore
├── README.md
├── requirements.txt


## How to Run

### Shell Mode (Recommended)
```bash
python main.py shell

# Single Command Logging
python main.py log

# Encrypt Logs
python main.py encrypt

# Decrypt Logs
python main.py decrypt

# Welcome Message
python main.py greet