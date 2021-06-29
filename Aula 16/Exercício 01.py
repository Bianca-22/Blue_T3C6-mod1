class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nomeP = nome
        self.idadeP = idade
        self.pesoP = peso
    def comer(self, calorias):
        if self.idadeP > 30:
            self.pesoP += (calorias*2)
        else:
            self.pesoP += calorias
    def malhar(self, calorias):
        if self.idadeP < 30:
            self.pesoP -= (calorias*2)
        else:
            self.pesoP -= calorias
    def mostrarDados(self):
        return f'''
        NOME: {self.nomeP}
        IDADE: {self.idadeP}
        Peso: {self.pesoP}
        '''

pessoa1 = Pessoa('Bianca', 20, 65)
pessoa2 = Pessoa('Angelica', 47, 75)

print(pessoa1.mostrarDados())
pessoa1.comer(5)
print(pessoa1.mostrarDados())
pessoa1.malhar(9)
print(pessoa1.mostrarDados())
print('-<'*15)
print(pessoa2.mostrarDados())
pessoa2.comer(5)
print(pessoa2.mostrarDados())
pessoa2.malhar(9)
print(pessoa2.mostrarDados())
