from src.modelos.ativo import Ativo
from src.modelos.vulnerabilidades import Vulnerabilidade
from src.modelos.validacoes import validar_texto_identificacao


class Roteador(Ativo):
    campo_especifico = "modelo"
    rotulo_campo = "Modelo"

    def __init__(self, id: int, nome: str, responsavel: str, setor: str,
                 vulnerabilidades: list[Vulnerabilidade], modelo: str) -> None:
        super().__init__(id, nome, responsavel, setor, vulnerabilidades)
        self.modelo = self.validar_campo_especifico(modelo)

    @staticmethod
    def validar_campo_especifico(valor: object) -> str:
        return validar_texto_identificacao(valor, "Modelo")

    def exibir_detalhes(self) -> None:
        super().exibir_detalhes_comuns()
        print(f"Modelo: {self.modelo}")

    def obter_tipo(self) -> str:
        return "Roteador"

    def obter_fator_exposicao(self) -> float:
        return 1.2  # borda da rede, mas com poucas portas de serviço