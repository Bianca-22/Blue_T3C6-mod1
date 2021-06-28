# Importando bibliotecas e suas funções
from random import randint
from operator import itemgetter
from time import sleep 

rodadas = []
jogador = {}
empates = []

num = int(input('Quantas rodadas você vai querer jogar? '))
# O For irá rodar conforme a quantidade de rodadas que o usuário escolher
for r in range(1,num+1):
    print('***'*20)
    print(f'{r}° RODADA')
    # Esse For é para a quantidade de jogadores
    for j in range(1,5):
        print('-<-'*20)
        print(f'{j}° JOGADOR')
        dado = randint(1,6)
        # Adicionando ao dicionário 'jogador' a chave (Jogador...) e o valor do dado
        jogador[f'Jogador {j}'] = dado
        print('ROLANDO OS DADOS')
        sleep(1)
        print(f'O dado caiu no número {dado}')
        jogador.copy()
    sorted(jogador.items(), key=itemgetter(1))
    # Esse For vai percorrer o dicionário até achar o maior valor
    for m in [max(jogador.values())]:
        empate = 0
        # A variavel key será a chave do dicionário e a variavel val será o valor
        for key,val in jogador.items():
            # Se o mesmo valor se repetir então dará empate
            if val == m:
                empate += 1
        # Se empatar então o empate será adicionado a lista 'empates'
        if empate >= 2:
            empates.append(empate)
            print('Empatado')
        # Senão, então o vencedor será adcionado a lista 'rodadas'
        else:
            rodadas.append(key)
            print(f'O vencedor da {r}° rodada é o', key)
# O count() é para contar a quantidade de vezes que o valor aparece
# O len() diz o tamanho dalista q será a quantidade de empates
print(f'''
O total de vitórias do Jogador 1 é de: {rodadas.count('Jogador 1')}
O total de vitórias do Jogador 2 é de: {rodadas.count('Jogador 2')}
O total de vitórias do Jogador 3 é de: {rodadas.count('Jogador 3')}
O total de vitórias do Jogador 4 é de: {rodadas.count('Jogador 4')}
O total de empates é de: {len(empates)}
''')