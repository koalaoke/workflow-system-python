import argparse
import time
from rich.prompt import Prompt
from src.domain.exceptions import TransicaoInvalidaError

class InteractiveParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

def pausar():
    input("\n[ENTER] para continuar...")

def list_process(args):
    lista = args.sistema.listar()
        
    for i, p in enumerate(lista):
        args.console.print(f"{i+1}. [{p.estado_atual}] {p.titulo}")

def create_process(args):
    titulo = Prompt.ask("Nome do processo: ")
    if titulo: args.sistema.criar(titulo)

def open_process(args):
    idx = int(args.id)
    processo = args.sistema.buscar(idx)
    if not processo:
        print("Processo não encontrado.")
        time.sleep(1)
        return
    console = args.console
    while True:
        console.print(f"🔧 GERENCIANDO: {processo.titulo}")
        console.print(f"🚦 ESTADO: [{processo.estado_atual}]")
        console.print("1. ✅ Aprovar / Avançar")
        console.print("2. ⛔ Rejeitar")
        console.print("3. 📜 Ver Histórico")
        console.print("0. 🔙 Voltar")
        
        op = console.input("\nOpção: ")
        
        try:
            if op == "1":
                processo.aprovar()
                console.print(">> Sucesso: Processo avançou.")
                time.sleep(1)
            elif op == "2":
                processo.rejeitar()
                console.print(">> Sucesso: Processo rejeitado.")
                time.sleep(1)
            elif op == "3":
                processo.ver_historico()
                pausar()
            elif op == "0":
                break
            else:
                console.print("Opção inválida.")
                time.sleep(0.5)
        except TransicaoInvalidaError as e:
            console.print(f"\n❌ ERRO DE REGRA: {e}")
            pausar()

process_parser = InteractiveParser(prog='process', add_help=False)
subparsers = process_parser.add_subparsers()

parser_new = subparsers.add_parser('new', help='new help')
parser_new.set_defaults(func=create_process)

parser_list = subparsers.add_parser('list', help='list help')
parser_list.set_defaults(func=list_process)

parser_open = subparsers.add_parser('open', help='open help')
parser_open.add_argument("id")
parser_open.set_defaults(func=open_process)