from src.workflow.estados.interface import EstadoProcesso
from src.workflow.exceptions import TransicaoInvalidaError
from src.workflow.processo import Processo


class EstadoAprovado(EstadoProcesso):
    """Aprovado: Processo finalizado com sucesso."""
    
    @property
    def nome(self) -> str:
        return "APROVADO"

    def aprovar(self, processo: 'Processo') -> None:
        # Se já está aprovado, não faz sentido aprovar de novo.
        raise TransicaoInvalidaError("O processo já está finalizado e aprovado.")

    def rejeitar(self, processo: 'Processo') -> None:
        raise TransicaoInvalidaError("O processo já está finalizado (aprovado) e não pode ser rejeitado.")


class EstadoRejeitado(EstadoProcesso):
    """Rejeitado: Processo negado."""
    
    @property
    def nome(self) -> str:
        return "REJEITADO"

    def aprovar(self, processo: 'Processo') -> None:
        raise TransicaoInvalidaError("Processo rejeitado não pode ser aprovado.")

    def rejeitar(self, processo: 'Processo') -> None:
        raise TransicaoInvalidaError("O processo já está rejeitado.")


class EstadoEmAnalise(EstadoProcesso):
    """
    O processo está sendo revisado.
    Daqui ele pode ir para APROVADO ou REJEITADO.
    """
    
    @property
    def nome(self) -> str:
        return "EM_ANALISE"

    def aprovar(self, processo: 'Processo') -> None:
        # A lógica de negócio diz: Se aprovar na análise, vai para Aprovado.
        processo.set_estado(EstadoAprovado())

    def rejeitar(self, processo: 'Processo') -> None:
        # A lógica de negócio diz: Se rejeitar na análise, vai para Rejeitado.
        processo.set_estado(EstadoRejeitado())


class EstadoCriado(EstadoProcesso):
    """
    Estado inicial.
    A única saída possível é ir para análise.
    """
    
    @property
    def nome(self) -> str:
        return "CRIADO"

    def aprovar(self, processo: 'Processo') -> None:
        # Regra: Um processo criado precisa passar por análise antes de ser aprovado.
        # Por isso, "aprovar" aqui significa "enviar para análise".
        processo.set_estado(EstadoEmAnalise())

    def rejeitar(self, processo: 'Processo') -> None:
        # Regra: Não faz sentido rejeitar algo que acabou de ser criado e ninguém viu.
        # Isso simula uma regra de negócio restritiva.
        raise TransicaoInvalidaError("Não é possível rejeitar um processo que acabou de ser criado. Envie para análise primeiro.")