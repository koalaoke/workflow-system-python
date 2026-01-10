from src.workflow.estados.interface import EstadoProcesso
from src.workflow.exceptions import TransicaoInvalidaError

class EstadoAprovado(EstadoProcesso):
    """Aprovado: Processo finalizado com sucesso."""

class EstadoRejeitado(EstadoProcesso):
    """Estado: Processo negado."""

class EstadoEmAnalise(EstadoProcesso):
    """
    O processo está sendo revisado.
    Daqui ele pode ir para APROVADO ou REJEITADO.
    """

class EstadoCriado(EstadoProcesso):
    """
    Estado inicial.
    A única saída possível é ir para análise.
    """