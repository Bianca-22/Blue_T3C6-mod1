import random

RED = "\033[1;31m"  #\
BLUE = "\033[1;34m" # \ Variaveis feitas para colorir   
GREEN = "\033[0;32m"# /
BOLD = "\033[;1m"   # 

pedra = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)     
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# As variaveis Pedra, Papel e Tesoura foram feitas para mostrar o 'desenho' das mãos
empate = comp = usuario = 0 # Variavel para contar a quantidade de vezes q o jogador e o PC ganharam 
j = ['Pedra', 'Papel', 'Tesoura']  # Lista com a variaveis pedra, papel e tesoura
print()
print(BOLD + '------- Vamos Jogar Jokenpô -------')
print()

while True:
    rodadas = int(input(BOLD + 'Digite quantas rodadas você deseja jogar: '))
    for i in range(rodadas): # O i é o contador que irá contar a quantidade de rodadas
        escolha = input(BOLD + 'Pedra, Papel ou Tesoura? ').strip().capitalize()
        random.shuffle(j) #opções para randomizar o pedido que será mostrado, com a biblioteca random 
        j1 = random.sample(j,1) #função .sample limita a quantidade de itens a ser mostrada e j1 é ua nova lista criada para armazenar esse determinado item da lista j
        for c in j1: # c é o contador que auxiliará na contagem da lista j1 
            if c == 'Pedra': # Se o contador for igual a "Pedra" então os if's abaixo serão executados
                if escolha == 'Pedra': # Se a escoha do usuário for Pedra então os prints abaixo serão executados
                    print(GREEN + pedra) # Aqui será printado o dsenho da mão na cor verde
                    print(BOLD + f'Empatou, o computador escolheu {c}') # Aqui será printado a escolha (aleatória) do PC
                    print(GREEN + pedra)# Aqui será printado o dsenho da mão na cor verde
                    empate += 1 # Se a escolha do usuário e o contador forem iguais então a variável empate vai ser adicionada +1
                elif escolha == 'Papel': # Se a escoha do usuário for Pepel então os prints abaixo serão executados
                    print(BLUE + papel)# Aqui será printado o dsenho da mão na cor azul
                    print(BOLD + f'Você ganhou, o computador escolheu {c}')# Aqui será printado a escolha (aleatória) do PC
                    print(GREEN + pedra)# Aqui será printado o dsenho da mão na cor verde
                    usuario += 1# Se a escolha do usuário for papel e o contador for pedra então a variável usuario vai ser adicionada +1
                elif escolha == 'Tesoura': # Se a escoha do usuário for Tesoura então os prints abaixo serão executados
                    print(RED + tesoura)# Aqui será printado o dsenho da mão na cor vermelho
                    print(BOLD + f'Você perdeu, o computador escolheu {c}')# Aqui será printado a escolha (aleatória) do PC
                    print(GREEN + pedra)# Aqui será printado o dsenho da mão na cor verde
                    comp += 1# Se a escolha do usuário for tesoura e o contador for pedra então a variável comp vai ser adicionada +1
                else:
                    print(BOLD + 'Escolha inválida') # Se o usuário não escolher Pedra, papel ou tesoura então esse print será executado
            elif c == 'Papel': # Se o contador for igual a "Pedra" então os if's abaixo serão executados
                if escolha == 'Papel':# Se a escoha do usuário for Pepel então os prints abaixo serão executados
                    print(BLUE + papel)# Aqui será printado o dsenho da mão na cor azul
                    print(BOLD + f'Empatou, o computador escolheu {c}')# Aqui será printado a escolha (aleatória) do PC
                    print(BLUE + papel)# Aqui será printado o dsenho da mão na cor azul
                    empate += 1# Se a escolha do usuário e o contador forem iguais então a variável empate vai ser adicionada +1
                elif escolha == 'Tesoura': # Se a escoha do usuário for Tesoura então os prints abaixo serão executados
                    print(RED + tesoura)# Aqui será printado o dsenho da mão na cor vermelha
                    print(BOLD + f'Você ganhou, o computador escolheu {c}')# Aqui será printado a escolha (aleatória) do PC
                    print(BLUE + papel)# Aqui será printado o dsenho da mão na cor azul
                    usuario += 1# Se a escolha do usuário for tesoura e o contador for papel então a variável usuario vai ser adicionada +1
                elif escolha == 'Pedra': # Se a escoha do usuário for Pedra então os prints abaixo serão executados
                    print(GREEN + pedra)# Aqui será printado o dsenho da mão na cor verde
                    print(BOLD + f'Você perdeu, o computador escolheu {c}')# Aqui será printado a escolha (aleatória) do PC
                    print(BLUE + papel)# Aqui será printado o dsenho da mão na cor azul
                    comp += 1# Se a escolha do usuário for pedra e o contador for papel então a variável comp vai ser adicionada +1
                else:
                    print(BOLD + 'Escolha inválida')# Se o usuário não escolher Pedra, papel ou tesoura então esse print será executado
            elif c == 'Tesoura': # Se o contador for igual a "Pedra" então os if's abaixo serão executados
                if escolha == 'Tesoura': # Se a escoha do usuário for Tesoura então os prints abaixo serão executados
                    print(RED + tesoura)# Aqui será printado o dsenho da mão na cor vermelha
                    print(BOLD + f'Empatou, o computador escolheu {c}')# Aqui será printado a escolha (aleatória) do PC
                    print(RED + tesoura)# Aqui será printado o dsenho da mão na cor vermelha
                    empate += 1# Se a escolha do usuário e o contador forem iguais então a variável empate vai ser adicionada +1
                elif escolha == 'Pedra': # Se a escoha do usuário for Pedra então os prints abaixo serão executados
                    print(GREEN + pedra)# Aqui será printado o dsenho da mão na cor verde
                    print(BOLD + f'Você ganhou, o computador escolheu {c}')# Aqui será printado a escolha (aleatória) do PC
                    print(RED + tesoura)# Aqui será printado o dsenho da mão na cor vermelha
                    usuario += 1# Se a escolha do usuário for pedra e o contador for tesoura então a variável usuario vai ser adicionada +1
                elif escolha == 'Papel':# Se a escoha do usuário for Pepel então os prints abaixo serão executados
                    print(BLUE + papel)# Aqui será printado o dsenho da mão na cor azul
                    print(BOLD + f'Você perdeu, o computador escolheu {c}')# Aqui será printado a escolha (aleatória) do PC
                    print(RED + tesoura)# Aqui será printado o dsenho da mão na cor vermelha
                    comp += 1# Se a escolha do usuário for papel e o contador for pepel então a variável comp vai ser adicionada +1
                else:
                    print(BOLD + 'Escolha inválida')# Se o usuário não escolher Pedra, papel ou tesoura então esse print será executado
    s_n = input(BOLD + 'Você deseja continuar?[S/N] ').strip().lower()[0] # Variável feita para perguntar ao jogador se ele quer continuar o jogo
    print()
    if s_n != 's': # Se o usuário der uma resposta diferente de "sim", então o jogo será finalizado
        break
    else: # Senão, o jogo irá continuar, voltando do inicio
        continue
print(BOLD + f'Você ganhou {usuario} rodadas e o computador ganhou {comp} rodadas.')# Aqui mostra a quantidade de vezes a o usuário e o PC ganharam
print()
if usuario == comp: # Se a variável usuario e comp forem iguais então o jogo ficará empatado
    print(BOLD + 'Vocês empataram.')
elif usuario <= comp:# Se a variável usuario for menor q a variável comp então o PC será o vencedor
    print(BOLD + 'O computador é o grande campeão!')
else:# Senão, então o usuário será o vencedor
    print(BOLD + 'Você foi o grande campeão. Parabéns!!')