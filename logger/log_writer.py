# logger/log_writer.py

import json
import os
import subprocess
from logger.utils import get_username,get_timestamp
from datetime import datetime

LOG_FILE = 'logs/command_log.json'

def save_history(command):
    with open("history.txt", "a") as f:
        f.write(f"{datetime.now().isoformat()} | {command}\n")

def log_command(command: str):
    save_history(command) 
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        status = "success" if result.returncode == 0 else "failure"
        output = result.stdout.strip()
        error = result.stderr.strip()
    except Exception as e:
        status = "Failure"
        output = ""
        error = str(e)
    log_entry = {
        "timestamp" : get_timestamp(),
        "user" : get_username(),
        "command" : command,
        "status" : status,
        "output" : output,
        "error" : error
    }
    print(f"[DEBUG] Writing to {LOG_FILE}")
    print(f"[DEBUG] Folder exists: {os.path.exists(os.path.dirname(LOG_FILE))}")


    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


    # 📝 Write or append
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r+', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

            data.append(log_entry)
            file.seek(0)
            json.dump(data, file, indent=4)
    else:
        with open(LOG_FILE, 'w', encoding='utf-8') as file:
            json.dump([log_entry], file, indent=4)

def save_history(command):
    with open("history.txt", "a") as f:
        f.write(f"{datetime.now().isoformat()} | {command}\n")
