from time import sleep

# Função criada para calcular a idade do usuario e saber se ele pode ou não votar
def autoriza_voto(ano_nasc):
    ano_nasc = 2021 - ano_nasc
    if ano_nasc < 16:
        return 'VOTO NEGADO'
    elif ano_nasc >= 18:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'
 
votos = []
#função  feita para adicionar os votos na lista e informar ao usuario em quem ele votou
def votacao(autorizacao, num=0):
    if autorizacao == 'VOTO OBRIGATÓRIO':
        if num == 1:
            votos.append(num)
            return 'Você votou no candidato Marlon com sucesso.'
        elif num == 2:
            votos.append(num)
            return 'Você votou no candidato Paulo com sucesso.'
        elif num == 3:
            votos.append(num)
            return 'Você votou na candidata Bianca com sucesso.'
        elif num == 4:
            votos.append(num)
            return 'Você optou pelo voto nulo com sucesso.'
        elif num == 5:
            votos.append(num)
            return 'Você optou pelo voto em branco com sucesso.'
        else:
            return 'Voto inválido. Tente novamente.'
    elif autorizacao == 'VOTO OPCIONAL':
        if num == 1:
            votos.append(num)
            return 'Você votou no candidato Marlon com sucesso.'
        elif num == 2:
            votos.append(num)
            return 'Você votou no candidato Paulo com sucesso.'
        elif num == 3:
            votos.append(num)
            return 'Você votou na candidata Bianca com sucesso.'
        elif num == 4:
            votos.append(num)
            return 'Você optou pelo voto nulo com sucesso.'
        elif num == 5:
            votos.append(num)
            return 'Você optou pelo voto em branco com sucesso.'
        else:
            return 'Voto inválido. Tente novamente.'
    else:
        return 'Você não pode votar.'

print('\n-+-+-+-+-+-+-+-+-+ As eleições chegaram! Vamos votar! -+-+-+-+-+-+-+-+-+')
print('\nPrimeiro diga seu ano de nascimento para verificarmos sua situação.')

while True:
    nasc = int(input('Digite seu ano de nascimento: '))
    # Nesse print eu mostro ao usuario se ele pode ou não votar
    print(autoriza_voto(nasc))
    # Se a situação do usuario for opcional, ele poderá escolher se quer ou não votar
    if autoriza_voto(nasc) == 'VOTO OPCIONAL':
        escolha = input('\nSeu voto é opcional, você deseja votar [S/N]? ').strip().lower()[0]
        if escolha == 's':
            print('\nÓtimo! Agora digite um dos números abaixo para validar seu voto.')
            print('1 - Candidato Marlon\n2 - Candidato Paulo\n3 - Candidata Bianca\n4 - Voto Nulo\n5 - Voto em Branco')
            num = int(input('Digite seu voto aqui: '))
            # Nessa função 'votacao()' eu ponho como um dos parâmetros a função 'autoriza_voto()' para mostrar em quem o usuario votou
            print(votacao(autoriza_voto(nasc), num))
        else:
            break
    elif autoriza_voto(nasc) == 'VOTO OBRIGATÓRIO':
        print('\nÓtimo! Agora digite um dos números abaixo para validar seu voto.')
        print('1 - Candidato Marlon\n2 - Candidato Paulo\n3 - Candidata Bianca\n4 - Voto Nulo\n5 - Voto em Branco')
        num = int(input('Digite seu voto aqui: '))
        print(votacao(autoriza_voto(nasc), num))
    else:
        print('Você não pode votar.')
    proximo = input('\nPróximo eleitor [S/N]? ').strip().lower()[0]
    if proximo != 's':
        break

m = votos.count(1)
p = votos.count(2)
b = votos.count(3)

print(f'\nO total de votos para o candidato Marlon é de: {m}\nO total de votos para o candidato Paulo é de: {p}\nO total de votos para a candidata Bianca é de: {b}\nO total de votos nulos é de: {votos.count(4)}\nO total de votos em branco é de: {votos.count(5)}')
# Se a variavel m for maior que a variavel p e b, então o vencedor da eleição será o Marlon
if m > b and m > p:
    print('\nQuem ganhou a eleição foi...')
    # Um leve suspense para saber o vencedor, com o sleep
    sleep(3)
    print(f'O candidato Marlon!!! Com {m}% dos votos')
# Se a variavel p for maior que a variavel m e b, então o vencedor da eleição será o Paulo
elif p > b and p > m:
    print('\nQuem ganhou a eleição foi...')
    sleep(3)
    print(f'O candidato Paulo!!! Com um total de {p} votos')
# Se a variavel b for maior que a variavel p e m, então o vencedor da eleição será a Bianca
elif b > m and b > p:
    print('\nQuem ganhou a eleição foi...')
    sleep(3)
    print(f'A candidata Bianca!!! Com um total de {b} votos')
