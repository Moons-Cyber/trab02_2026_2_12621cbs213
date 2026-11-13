from src.modelos.ativo import Ativo
from src.modelos.vulnerabilidades import Vulnerabilidade
from src.modelos.validacoes import validar_memoria_ram


class Notebook(Ativo):
    campo_especifico = "memoria_ram"
    rotulo_campo = "Memória RAM"

    def __init__(self, id: int, nome: str, responsavel: str, setor: str,
                 vulnerabilidades: list[Vulnerabilidade], memoria_ram: str) -> None:
        super().__init__(id, nome, responsavel, setor, vulnerabilidades)
        self.memoria_ram = self.validar_campo_especifico(memoria_ram)

    @staticmethod
    def validar_campo_especifico(valor: object) -> str:
        return validar_memoria_ram(valor)

    def exibir_detalhes(self) -> None:
        super().exibir_detalhes_comuns()
        print(f"Memória RAM: {self.memoria_ram}")

    def obter_tipo(self) -> str:
        return "Notebook"

    def obter_fator_exposicao(self) -> float:
        return 1.0  # referência: usuário final, atrás da rede interna