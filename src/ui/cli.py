import time
from rich.console import Console
from src.services.manager import GerenciadorDeProcessos
from src.domain.exceptions import TransicaoInvalidaError

# Instância do sistema
sistema = GerenciadorDeProcessos()

def pausar():
    input("\n[ENTER] para continuar...")

def menu_processo(console ,processo):
    while True:
        console.clear()
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

def menu_principal():
    sistema.criar("Aquisição de Notebooks")
    
    console = Console()
    while True:
        console.print()
        console.clear()
        print("=== SISTEMA WORKFLOW ===")
        lista = sistema.listar()
        
        for i, p in enumerate(lista):
            console.print(f"{i+1}. [{p.estado_atual}] {p.titulo}")
            
        print("-" * 30)
        print("N. Novo Processo")
        print("0. Sair")
        
        op = console.input("\nEscolha (Número ou Letra): ").upper()
        
        if op == "0":
            break
        elif op == "N":
            titulo = input("Nome do processo: ")
            if titulo: sistema.criar(titulo)
        elif op.isdigit():
            idx = int(op)
            proc = sistema.buscar(idx)
            if proc:
                menu_processo(console, proc)
            else:
                print("Processo não encontrado.")
                time.sleep(1)