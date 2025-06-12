# Military Command Logger

A secure and interactive command logging tool built in Python using Typer and Rich. This project allows users to log terminal commands (custom or system), view logs in a structured format, and optionally encrypt/decrypt those logs for secure storage and analysis. It is designed with military or mission-critical applications in mind, where logging integrity and auditability are important.

## Features

- Interactive CLI interface with Rich and Typer
- Real-time system command execution using `subprocess`
- Logs commands with timestamp, username, and status to a JSON file
- Custom simulated commands like `run` and `halt`
- Secure encryption and decryption of the log file using `cryptography`
- Tracks user command history in a separate file
- Modular code structure for maintainability

## Technologies Used

- Python 3.11+
- Typer (for building the CLI)
- Rich (for styled terminal output)
- Cryptography (for encrypting and decrypting log files)

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
├── main.py
├── history.txt
├── .env
├── .gitignore
├── README.md
├── requirements.txt

