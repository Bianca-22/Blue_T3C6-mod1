#(DESAFIO) Crie um jogo onde o computador vai “pensar” em um número entre
# 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os
# palpites diga ao jogador se o número do computador é maior ou menor ao que ele
# digitou,no final mostre quantos palpites foram necessários para vencer.

from random import randint
comp = randint(0,20)
palpites = 0
usuario = int(input('Tente adivinhar o número entre 0 e 20: '))

while usuario != comp:
    palpites += 1
    if usuario >= comp:
        print('Menos...')
    else:
        print('Mais...')
    usuario = int(input('Tente adivinhar o número entre 0 e 20: '))
print(f'Parabéns, você acertou com {palpites} palpites.')