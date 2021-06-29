#Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos 
#Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos 
#implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, 
#caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."

class Conta:
    def __init__(self, titular, saldo):
        self.titularP = titular
        self.saldoP = saldo
    def sacar(self,retirada):
        if self.saldoP < 0:
            return 'Você não tem saldo suficiente para essa operação.'
        else:
            self.saldoP -= retirada
    def depositar(self, deposito):
        self.saldoP += deposito
    def mostrarDados(self):
        return f'''
        Nome do titular: {self.titularP}
        Saldo da conta: {self.saldoP}
        '''

x = Conta('Bianca', 600)
print(x.mostrarDados())
x.sacar(int(input('Quanto deseja sacar? ')))
print(x.mostrarDados())
x.depositar(int(input('Quanto deseja depositar? ')))
print(x.mostrarDados())