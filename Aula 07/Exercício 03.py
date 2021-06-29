#03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
#maiores.

ano = 2021
maior = 0
menor = 0

for nasc in range(7):
  nasc = int(input('digite seu ano de nascimento: '))
  b = ano - nasc
  if b > 18:
    maior += 1
  else:
    menor += 1
print(f'{maior} pessoas são maiores de idade\n{menor} pessoas são menores de idade')