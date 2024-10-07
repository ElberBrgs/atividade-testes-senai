from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario


class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str,crm:str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self,valor) -> float:
        valor = 7000
        return valor

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCRM: {self.crm}"
            )
    