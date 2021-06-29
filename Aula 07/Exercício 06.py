# - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

cont = 0
homem = 0
idade_mulher = 0

while True:
    sexo = input('Digite o sexo biológico [F/M]: ').strip().lower()[0]
    idade = int(input('Digite a idade: '))
    if sexo == 'm':
        homem += 1
        if idade >= 18:
            cont += 1
    if sexo == 'f':
        if idade >= 18:
            cont += 1
        if idade <= 20:
            idade_mulher += 1
    resp = input('Quer continuar? ').strip().lower()[0]
    if resp != 's':
        break

print(f'''
{cont} pessoas tem mais de 18 anos.
{homem} homens foram cadastrados.
{idade_mulher} mulheres tem menos de 20 anos.
''')