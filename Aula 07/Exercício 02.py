#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
#tabuada desse número.

n = int(input('Digite o número para realizar a tabuada: '))
for b in range(1,11):
  print(f'{n} x {b} = {n*b}')