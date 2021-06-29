sexo = input('Digite o seu sexo biologico [F/M]:').upper()[0]

while sexo not in 'FM':
    print('Sexo biológico inválido.')
    sexo = input('Digite o seu sexo biologico novamente [F/M]:').upper()[0]
if sexo == 'F':
    print('Feminino')
elif sexo == 'M':
    print('Masculino')