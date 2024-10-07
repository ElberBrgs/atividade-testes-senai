import pytest

from projeto.models.endereco import Endereco
from projeto.models.medico import Medico

@pytest.fixture
def medico_valido():
    return Medico("Josefa","(27)99557-6300","josefa_baptista@gamil.com","6587423145",
                      Endereco("Avenida Carlos Lindenberg","289","Cobi de Cima","29117-730","Vila Velha"))

def test_nome_valido(medico_valido):
    assert medico_valido.nome == "Josefa"

def test_telefone_valido(medico_valido):
    assert medico_valido.telefone == "(27)99557-6300"

def test_email_valido(medico_valido):
    assert medico_valido.email == "josefa_baptista@gamil.com"

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "6587423145"

def test_logradouro_valido(medico_valido):
    assert medico_valido.endereco.logradouro == "Avenida Carlos Lindenberg"

def test_numero_valido(medico_valido):
    assert medico_valido.endereco.numero == "289"

def test_complemento_valido(medico_valido):
    assert medico_valido.endereco.complemento == "Cobi de Cima"

def test_cep_valido(medico_valido):
    assert medico_valido.endereco.cep == "29117-730"

def test_cidade_valida(medico_valido):
    assert medico_valido.endereco.cidade == "Vila Velha"