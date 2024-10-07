from projeto.models.endereco import Endereco
from abc import abstractmethod,ABC

@abstractmethod
class Funcionario(ABC):
    def __init__(self,nome:str,telefone:str,email:str,endereco:Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def salario_final(self,valor)->float:
        return valor
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nEndereço: {self.endereco}"
            f"\nSalário: {self.salario_final}"
            )