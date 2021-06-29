# Crie uma lista composta que recebe 5 nomes e 5 idades de  clientes, utilizando o for e o if, verifique quais clientes 
# são maiores de idade e quais são menores de idade e mostre  na tela a seguinte frase para cada um deles: 'Fulano é maior
# de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.

lista = []
maior = menor = 0
for c in range(5):
    clientes = []
    nome = input('Diga seu nome: ')
    idade = int(input('Diga sua idade: '))
    clientes.append(nome)
    clientes.append(idade)
    lista.append(clientes[:])
for b in lista:
    if b[1] >= 18:
        print(f'{b[0]} é maior de idade.')
        maior += 1
    else: 
        print(f'{b[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores de idade e {menor} menores de idade.')
