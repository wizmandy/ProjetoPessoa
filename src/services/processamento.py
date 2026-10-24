from datetime import date
from src.models.pessoa import Pessoa
from src.models.pessoa_arquivo import ArquivoPessoa

def criar_pessoa():
    return Pessoa("Maria", date(2000, 12, 2))

def criar_arquivo():
    return ArquivoPessoa("Carlos", date(1980, 12, 23))