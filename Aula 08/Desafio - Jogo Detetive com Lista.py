'''
Desafio da noite:
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''

resp = []

resp.append(input('Telefonou para a vítima [S/N]? ').upper()[0])
resp.append(input('Esteve no local do crime [S/N]? ').upper()[0])
resp.append(input('Mora perto da vítima [S/N]? ').upper()[0])
resp.append(input('Devia para a vítima [S/N]? ').upper()[0])
resp.append(input('Ja trabalhou com a vítima [S/N]? ').upper()[0])

resp_sim = resp.count('S')

if resp_sim == 2:
  print('Suspeita')
elif resp_sim == 3 and resp_sim == 4:
  print('Cúmplice')
elif resp_sim == 5:
  print('Assassino')
else:
  print('Inocente')