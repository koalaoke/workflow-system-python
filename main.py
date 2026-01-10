# main.py (Na raiz do projeto)

# Importamos a função que inicia o loop do menu visual
from src.ui.cli import menu_principal

# Verificamos se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    menu_principal()