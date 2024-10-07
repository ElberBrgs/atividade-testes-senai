import pytest

from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro

@pytest.fixture
def engenheiro_valido():
    return Engenheiro("Josefa","(27)99557-6300","josefa_baptista@gamil.com","6587423145",
                      Endereco("Avenida Carlos Lindenberg","289","Cobi de Cima","29117-730","Vila Velha"))

def test_nome_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "Josefa"

def test_telefone_valido(engenheiro_valido):
    assert engenheiro_valido.telefone == "(27)99557-6300"

def test_email_valido(engenheiro_valido):
    assert engenheiro_valido.email == "josefa_baptista@gamil.com"

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "6587423145"

def test_logradouro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.logradouro == "Avenida Carlos Lindenberg"

def test_numero_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.numero == "289"

def test_complemento_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.complemento == "Cobi de Cima"

def test_cep_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cep == "29117-730"

def test_cidade_valida(engenheiro_valido):
    assert engenheiro_valido.endereco.cidade == "Vila Velha"