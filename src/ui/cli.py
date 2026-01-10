import os
import time
from src.services.manager import GerenciadorDeProcessos
from src.domain.exceptions import TransicaoInvalidaError

# Instância do sistema
sistema = GerenciadorDeProcessos()

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\n[ENTER] para continuar...")

def menu_processo(processo):
    while True:
        limpar()
        print(f"🔧 GERENCIANDO: {processo.titulo}")
        print(f"🚦 ESTADO: [{processo.estado_atual}]")
        print("1. ✅ Aprovar / Avançar")
        print("2. ⛔ Rejeitar")
        print("3. 📜 Ver Histórico")
        print("0. 🔙 Voltar")
        
        op = input("\nOpção: ")
        
        try:
            if op == "1":
                processo.aprovar()
                print(">> Sucesso: Processo avançou.")
                time.sleep(1)
            elif op == "2":
                processo.rejeitar()
                print(">> Sucesso: Processo rejeitado.")
                time.sleep(1)
            elif op == "3":
                processo.ver_historico()
                pausar()
            elif op == "0":
                break
            else:
                print("Opção inválida.")
                time.sleep(0.5)
        except TransicaoInvalidaError as e:
            print(f"\n❌ ERRO DE REGRA: {e}")
            pausar()

def menu_principal():
    # Dados iniciais para teste
    sistema.criar("Aquisição de Notebooks")
    
    while True:
        limpar()
        print("=== SISTEMA WORKFLOW ===")
        lista = sistema.listar()
        
        for i, p in enumerate(lista):
            print(f"{i+1}. [{p.estado_atual}] {p.titulo}")
            
        print("-" * 30)
        print("N. Novo Processo")
        print("0. Sair")
        
        op = input("\nEscolha (Número ou Letra): ").upper()
        
        if op == "0":
            break
        elif op == "N":
            titulo = input("Nome do processo: ")
            if titulo: sistema.criar(titulo)
        elif op.isdigit():
            idx = int(op)
            proc = sistema.buscar(idx)
            if proc:
                menu_processo(proc)
            else:
                print("Processo não encontrado.")
                time.sleep(1)