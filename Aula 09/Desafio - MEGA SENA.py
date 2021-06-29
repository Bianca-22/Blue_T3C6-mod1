'''
Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
'''

from random import randint
from time import sleep
jogos = []
lista = [] # Poderia declarar essa variavel dentro do for e não precisaria usar o clear()
qnt = int(input('Digite a quantidade de jogos: '))

for b in range(1,qnt+1):
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print(f'\n----- {qnt} jogos sorteados -----')
print()
for i ,c in enumerate(jogos):
    print(f'O {i+1}° jogo sorteado foi: {c}')
    sleep(2)
