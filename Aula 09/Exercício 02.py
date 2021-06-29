'''
02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
geradas.
'''

lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2:
        pares.append(n)
    else:
        impares.append(n)
    resp = input('Quer continuar?(S/N) ').strip().lower()[0]
    if resp == 'n':
        break
print(lista)
print(pares)
print(impares)
