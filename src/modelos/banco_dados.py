from src.modelos.ativo import Ativo
from src.modelos.vulnerabilidades import Vulnerabilidade
from src.modelos.validacoes import validar_texto_identificacao


class BancoDeDados(Ativo):
    campo_especifico = "sgbd"
    rotulo_campo = "SGBD"

    def __init__(self, id: int, nome: str, responsavel: str, setor: str,
                 vulnerabilidades: list[Vulnerabilidade], sgbd: str) -> None:
        super().__init__(id, nome, responsavel, setor, vulnerabilidades)
        self.sgbd = self.validar_campo_especifico(sgbd)

    @staticmethod
    def validar_campo_especifico(valor: object) -> str:
        return validar_texto_identificacao(valor, "SGBD")

    def exibir_detalhes(self) -> None:
        super().exibir_detalhes_comuns()
        print(f"SGBD: {self.sgbd}")

    def obter_tipo(self) -> str:
        return "BancoDeDados"

    def obter_fator_exposicao(self) -> float:
        return 1.0  # normalmente atrás da aplicação; o risco vem pela dependência