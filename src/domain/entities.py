from typing import List, Dict, Any
from dataclasses import dataclass, asdict
from datetime import datetime
from src.domain.interfaces import EstadoProcesso
from src.domain.exceptions import TransicaoInvalidaError
from src.domain import states

# COMPONENTE DE HISTÓRICO
@dataclass(frozen=True)
class Registro:
    data: datetime
    mensagem: str
    estado_anterior: str
    novo_estado: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "data": self.data.isoformat(),
            "mensagem": self.mensagem,
            "estado_anterior": self.estado_anterior,
            "novo_estado": self.novo_estado
        }

class Historico:
    def __init__(self):
        self._entradas: List[Registro] = []

    def adicionar(self, mensagem: str, estado_anterior: str, novo_estado: str) -> None:
        self._entradas.append(Registro(
            data=datetime.now(),
            mensagem=mensagem,
            estado_anterior=estado_anterior,
            novo_estado=novo_estado
        ))

    def imprimir_na_tela(self) -> None:
        print("\n--- Histórico de Eventos ---")
        for reg in self._entradas:
            data_fmt = reg.data.strftime("%H:%M:%S")
            print(f"[{data_fmt}] {reg.estado_anterior} -> {reg.novo_estado} : {reg.mensagem}")
        print("----------------------------\n")

# ENTIDADE PRINCIPAL
class Processo:
    def __init__(self, titulo: str, estado_inicial: EstadoProcesso):
        self._titulo = titulo
        self._estado = estado_inicial
        self._historico = Historico()
        
        # Log inicial
        self._historico.adicionar("Criação do Processo", "N/A", estado_inicial.nome)

    @property
    def estado_atual(self) -> str:
        return self._estado.nome

    @property
    def titulo(self) -> str:
        return self._titulo

    def set_estado(self, novo_estado: EstadoProcesso) -> None:
        estado_anterior = self._estado.nome
        self._estado = novo_estado
        
        self._historico.adicionar(
            "Mudança de Estado", estado_anterior, novo_estado.nome
        )

    def aprovar(self) -> None:
        # Delega para o estado (Polimorfismo)
        self._estado.aprovar(self)

    def rejeitar(self) -> None:
        # Delega para o estado (Polimorfismo)
        self._estado.rejeitar(self)
    
    def ver_historico(self) -> None:
        self._historico.imprimir_na_tela()