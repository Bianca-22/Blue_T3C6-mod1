'''
01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.
'''

num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
    resp = input('Você quer continuar? ').strip().lower()[0]
    if resp == 'n':
        break
print(f'A lista ordenada é: {num}')
