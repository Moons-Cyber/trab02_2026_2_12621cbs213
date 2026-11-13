from src.modelos.ativo import Ativo
from src.modelos.vulnerabilidades import Vulnerabilidade
from src.modelos.validacoes import validar_texto_identificacao


class Servidor(Ativo):
    campo_especifico = "processador"
    rotulo_campo = "Processador"

    def __init__(self, id: int, nome: str, responsavel: str, setor: str,
                 vulnerabilidades: list[Vulnerabilidade], processador: str) -> None:
        super().__init__(id, nome, responsavel, setor, vulnerabilidades)
        self.processador = self.validar_campo_especifico(processador)

    @staticmethod
    def validar_campo_especifico(valor: object) -> str:
        return validar_texto_identificacao(valor, "Processador")

    def exibir_detalhes(self) -> None:
        super().exibir_detalhes_comuns()
        print(f"Processador: {self.processador}")

    def obter_tipo(self) -> str:
        return "Servidor"

    def obter_fator_exposicao(self) -> float:
        return 1.5  # serviços publicados na rede