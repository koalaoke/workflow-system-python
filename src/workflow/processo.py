from typing import List
from src.workflow.estados.interface import EstadoProcesso

class Processo:
    """
    Representa o contexto no State Pattern.
    Mantém uma referência para uma instância de EstadoProcesso atual.
    """

    def __init__(self, titulo: str, estado_inicial: EstadoProcesso):
        self._titulo = titulo
        self._estado = EstadoProcesso = estado_inicial
        self._historico: List[str] = []

        self._registrar_historico(f"Processo criado em estado: {self._estado.nome}")
    
    @property
    def estado_atual(self) -> str:
        """Retorna o nome do estado atual (Apenas leitura)."""
        return self._estado.nome
    
    def set_estado(self, novo_estado: EstadoProcesso) -> None:
        """Método usado pelos objetos de Estado para atualizar a referência.
        Permite a transição de estados.
        """
        print(f"--- Transição: {self._estado.nome} -> {novo_estado.nome} ---")
        self._estado = novo_estado
        self._registrar_historico(f"Transição para: {novo_estado.nome}")

        def aprovar(self) -> None:
            self._estado.aprovar(self)

        def rejeitar(self) -> None:
            self._estado.rejeitar(self)

        def _registrar_historico(self, mensagem: str) -> None:
            self._historico.append(mensagem)
            print(f"[Log]: {mensagem}")
