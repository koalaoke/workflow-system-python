import shlex
import argparse
from .process import process_parser
from rich.console import Console
from src.services.manager import GerenciadorDeProcessos

sistema = GerenciadorDeProcessos()

def menu_principal():
    sistema.criar("Aquisição de Notebooks")    
    console = Console()

    process_parser.set_defaults(sistema=sistema, console=console)

    while True:
        try:   
            raw_input = console.input("[cyan](workflow) >")
            user_command = shlex.split(raw_input)

            match user_command[0]:
                case "help":
                    console.rule("[white bold]Workflow - Seus sistema de processos.")
                    console.print("help - Exibe ajuda.")
                    console.print("process list - Exibe os processos.")
                    console.print("process new - Cria processo.")
                    console.print("process <id> - Exibe um processo.")
                    console.print("clear - Limpa o console.")
                    console.print("exit - sai do sistema.")

                case "process":
                    try:
                        args = process_parser.parse_args(user_command[1:])
                        if hasattr(args, 'func'):
                            args.func(args)
                        else:
                            process_parser.print_help()

                    except ValueError as e:
                        console.print(e)

                    except SystemExit:
                        pass


                case "clear":
                    console.clear()
                    console.print()

                case "exit":
                    break
                case _:
                    print("Comando não reconhecido. Use help para ver os comandos disponíveis")
        
        except KeyboardInterrupt:
            break
