# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato
                                #INCOMPLETO
cont = 0
precoTotal = 0
while True:
    nome = input('Digite o nome do produto: ')
    precoProduto = float(input('Digite o preço do produto: '))
    precoTotal = precoProduto + precoTotal
    if precoProduto >= 1000:
        cont += 1
    resp = input('Quer continuar [S/N]? ').strip().lower()[0]
    if resp != 's':
        break
print(f'''
O total gasto na compra é de: {precoTotal}
{cont} produtos custam mais de R$ 1000
O nome do produto mais barato é:
''')