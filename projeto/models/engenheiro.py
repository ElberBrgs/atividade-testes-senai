from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario


class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str,crea:str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self,valor) -> float:
        valor = 5000
        return valor

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCREA: {self.crea}"
            )
    