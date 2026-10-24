from datetime import date

class Pessoa:
    def __init__(self, nome, data_nascimento, data_atual=None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.data_atual = data_atual or date.today()
        self.idade = self.calcular_idade()

    def calcular_idade(self):
        idade = self.data_atual.year - self.data_nascimento.year
        if (self.data_atual.month, self.data_atual.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
        return idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e minha idade é de {self.idade} anos. Muito prazer!"