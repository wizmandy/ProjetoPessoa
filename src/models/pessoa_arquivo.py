from datetime import date, datetime
from pathlib import Path

PASTA_ARQUIVOS = Path(__file__).resolve().parents[2] / "arquivos_pessoa"
print(PASTA_ARQUIVOS)   

class ArquivoPessoaErro(Exception):
    pass

class ArquivoPessoa:
    def __init__(self, nome, data_nascimento, data_atual=None):
         if not nome:
              raise ArquivoPessoaErro("O nome da pessoa não pode estar vazio!")
         if not isinstance(data_nascimento, date):
              raise ArquivoPessoaErro("Data de nascimento deve ser uma data")

         self.nome = nome
         self.data_nascimento = data_nascimento
         self.data_atual = data_atual or date.today()

         if self.data_nascimento > self.data_atual:
              raise ArquivoPessoaErro("A data de nascimento não pode ser uma data futura. Por favor, corrija!")

         self.idade = self.calcular_idade()

    def calcular_idade(self):
        idade = self.data_atual.year - self.data_nascimento.year
        if(self.data_atual.month, self.data_atual.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
        return idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e minha idade é de {self.idade} anos. Muito prazer!"

    def salvar(self):
        try:
            PASTA_ARQUIVOS.mkdir(exist_ok=True)
            nome_arquivo = datetime.now().strftime("%Y%m%d_%H-%M-%S") + ".txt"
            caminho = PASTA_ARQUIVOS / nome_arquivo
            caminho.write_text(self.apresentar(), encoding="utf-8")
            return caminho
        except OSError as error:
            raise ArquivoPessoaErro(f"Não foi possível salvar o arquivo: {error}.")