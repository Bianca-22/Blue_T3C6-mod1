# (DESAFIO) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
# Os códigos utilizados são:
# 1 , 2, 3 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - José / 2- João / etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos


lista = []
while True:
    print('''
[1] - Marlon
[2] - Angelica
[3] - Tili
[4] - Bianca
[5] - Voto Nulo
[6] - Voto em Branco
''')
    usuario = int(input('Digite o seu voto: '))
    lista.append(usuario)
    resp = input('Quer continuar? ').strip().lower()[0]
    if resp != 's':
        break

totalVotos = len(lista)
votoNulo = lista.count(5)
votoBranco = lista.count(6)
porcentagemNulo = (totalVotos/(100*votoNulo))
porcentagemBranco = (totalVotos/(100*votoBranco))

print(f'''
O total de votos para o Marlon é de: {lista.count(1)}
O total de votos para a Angelica é de: {lista.count(2)}
O total de votos para a Tili é de: {lista.count(3)}
O total de votos para a Bianca é de: {lista.count(4)}
O total de votos nulos é de: {lista.count(5)}
O total de votos em branco é de:{lista.count(6)}
A porcentagem de votos nulos sobre o total de votos é de: {porcentagemNulo:.2f}%
A porcentagem de votos em branco sobre o total de votos é de: {porcentagemBranco:.2f}%
''')