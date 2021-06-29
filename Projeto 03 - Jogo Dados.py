# Importando bibliotecas e suas funções
from random import randint
from time import sleep 

jogador = {}
num = int(input('Quantas rodadas você vai querer jogar? '))
# O For irá rodar conforme a quantidade de rodadas que o usuário escolher
for r in range(1,num+1):
    print('\n***'*20)
    print(f'{r}° RODADA')
    # Esse For é para a quantidade de jogadores
    for j in range(1,5):
        print('\n-<-'*20)
        print(f'{j}° JOGADOR')
        dado = randint(1,6)
        # Adicionando ao dicionário 'jogador' a chave (Jogador...) e o valor do dado
        jogador[f'Jogador {j}'] = dado
        print('ROLANDO OS DADOS')
        sleep(1)
        print(f'O dado caiu no número {dado}')
        jogador.copy()
    print('\n---'*20)
    if jogador['jogador2'] < jogador['jogador1'] > jogador['jogador3'] and jogador['jogador1'] > jogador['jogador4']:
        situacao = 'jogador1'
        play1 += 1
    elif jogador['jogador1'] < jogador['jogador2'] > jogador['jogador3'] and jogador['jogador2'] > jogador['jogador4']:
        situacao = 'jogador2'
        play2 += 1
    elif jogador['jogador1'] < jogador['jogador3'] > jogador['jogador2'] and jogador['jogador3'] > jogador['jogador4']:
        situacao = 'jogador3'
        play3 += 1
    elif jogador['jogador2'] < jogador['jogador4'] > jogador['jogador3'] and jogador['jogador4'] > jogador['jogador1']:
        situacao = 'jogador4'
        play4 += 1
    else:
        situacao = 'Empate'
    print(f'O ganhador da rodada é o {situacao}\n')
if play2 < play1 > play3 and play1 > play4:
    print(f'        O campeão foi o Jogador 1 com {play1} Vitorias')
elif play1 < play2 > play3 and play2 > play4:
    print(f'        O campeão foi o Jogador 1 com {play2} Vitorias')
elif play1 < play3 > play2 and play3 > play4:
    print(f'        O campeão foi o Jogador 1 com {play3} Vitorias')
elif play2 < play4 > play3 and play4 > play1:
    print(f'        O campeão foi o Jogador 1 com {play4} Vitorias')
else:
    print('O resultado terminou em empate.')
