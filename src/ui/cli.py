import shlex
import argparse
from .process import process_parser
from rich.console import Console
from src.services.manager import GerenciadorDeProcessos

sistema = GerenciadorDeProcessos()

def menu_principal():
    sistema.criar("Aquisição de Notebooks")
    
    console = Console()
    while True:
        
        raw_input = console.input("(workflow) >")
        user_command = shlex.split(raw_input)

        match user_command[0]:
            case "help":
                console.print("Workflow - Seus sistema de processos.")
                console.print("help - Exibe ajuda.")
                console.print("process list- Exibe os processos.")
                console.print("process new - Cria processo.")
                console.print("process <id> - Exibe um processo.")
                console.print("clear - Limpa o console.")
                console.print("exit - sai do sistema.")

            case "process":
                process_parser.set_defaults(sistema=sistema, console=console)
                args = process_parser.parse_args(user_command[1:])
                args.func(args)

            case "clear":
                console.clear()
                console.print()

            case "exit":
                break
            case _:
                print("Comando não reconhecido. Use ")