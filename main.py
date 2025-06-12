# main.py
import typer
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from logger.log_writer import log_command
from logger.utils import get_username
from logger.encryptor import encrypt_log, decrypt_log  # Optional encryption commands

app = typer.Typer()
#run the command using the available commands
@app.command()
def shell():
    """
    Run Command Logger in interactive shell mode.
    """
    print("[bold green]Interactive Shell Activated[/bold green] 🟢")
    print("Type 'exit' to quit.\n")

    user = get_username()
    while True:
        command = Prompt.ask(f"[cyan]{user} >>>[/cyan]").strip()

        if command.lower() == "exit":
            print("[red]Exiting Shell...[/red] 🟥")
            break

        if command in ["run", "halt"]:
            output = {
                "run": "Military operation simulation started",
                "halt": "All systems halted"
            }[command]

            log_command(command, output, "", "success")
            print(f"[green]Custom command executed:[/green] {output}")
        else:
            log_command(command)
            print(f"[blue]System command logged:[/blue] '{command}'")

console = Console()

@app.command()
def themed():
    """
    Test colored themed output.
    """
    console.print("[bold yellow on black]⚔️  Tactical Command Logger Activated  ⚔️[/bold yellow on black]")
    console.print("[cyan]Use this interface to monitor mission commands and status[/cyan]")

@app.command()
def log():
    """
    Log a terminal command (system or custom).
    """
    user = get_username()
    print(f"[bold green]Hello, {user}![/bold green] 🫡")
    command = Prompt.ask("[cyan]Enter your command[/cyan]")

    if command in ["run", "halt"]:
        # custom command setter
        output = {
            "run": "Military operation simulation started",
            "halt": "All systems halted"
        }[command]

        log_command(command, output, "", "success")
        print(f"[green]Custom command executed:[/green] {output}")
    else:
        log_command(command)  # Using subprocess to run and log all the commands processed
        print(f"[blue]System command logged:[/blue] '{command}'")
# initial greeting of the program
@app.command()
def greet():
    """
    Display welcome message.
    """
    print("[bold magenta]Welcome to the Military Command Logger 🛡️[/bold magenta]")
#Encrypting code from the cryptography library
@app.command()
def encrypt():
    """
    Encrypt the log file (secure mode).
    """
    encrypt_log()
    print("[yellow]Log file encrypted successfully.[/yellow] 🔐")
#it's equivalent decryption code
@app.command()
def decrypt():
    """
    Decrypt the log file (for analysis).
    """
    decrypt_log()
    print("[yellow]Log file decrypted.[/yellow] 🧪")
#initializing the app/program
if __name__ == "__main__":
    app()
