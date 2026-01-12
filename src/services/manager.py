from typing import List, Optional
from src.domain.entities import Processo
from src.domain.states import EstadoCriado

class GerenciadorDeProcessos:
    def __init__(self):
        self._processos: List[Processo] = []
        self._contador = 1

    def criar(self, titulo: str) -> Processo:
        novo = Processo(f"#{self._contador} - {titulo}", EstadoCriado())
        self._processos.append(novo)
        self._contador += 1
        return novo

    def listar(self) -> List[Processo]:
        return self._processos

    def buscar(self, indice: int) -> Optional[Processo]:
        if 1 <= indice <= len(self._processos):
            return self._processos[indice - 1]
        return None