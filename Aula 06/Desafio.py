from random import randint
a = randint(1,20)
palpites = 0
n = int(input('Tente acertar o número entre 1 e 20: '))

while n != a:
   if  n < a:
     print('Mais...')
     palpites += 1
     n = int(input('Tente acertar o número: '))
   else:
     print('Menos...')
     palpites += 1
     n = int(input('Tente acertar o número: '))
print(f'Você acertou, com {palpites} palpites.')