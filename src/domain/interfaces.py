from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Este import só acontece enquanto o editor analisa o código,
    # mas é ignorado quando o programa roda de verdade.
    from src.workflow.processo import Processo

class EstadoProcesso(ABC):
    """
    Interface que define o contrato para todos os estados. Cada método representa uma ação possível no workflow. 
    """

    @property
    @abstractmethod
    def nome(self) -> str:
        """Retorna o nome legível do estado."""
        pass

    @abstractmethod
    def aprovar(self, processo: 'Processo') -> None:
        """
        Tenta mover o processo para o próximo estágio de aprovação.

        Args:
            processo: O objeto de contexto (Processo) que contém este estado.
        Raises: TransicaoInvalidaError: Se a ação não for permitida no estado atual 
        """
        pass

    @abstractmethod
    def rejeitar(self, processo: 'Processo') -> None:
        """
        Tenta rejeitar o processo.
        """
        pass

    def __str__(self) -> str:
        return self.nome
