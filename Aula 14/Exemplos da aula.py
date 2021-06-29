#Ex 05:
galera = []
pessoa = {}
soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).lower()[0]
        if pessoa['sexo'] in 'fm':
            break
        print('ERRO: Digite apenas F ou M.')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    soma += pessoa['idade']
    while True:
        resp = str(input('Continuar? ')).lower()[0]
        if resp in 'sn':
            break
        print('Digite apenas S ou N.')
    if resp == 'n':
        break
print(galera)
print(f'Temos um total de {len(galera)} pessoas cadastradas.')
media = soma/len(galera)
print(f'A média de idade é de: {media} anos')
print(f'O total de mulheres cadastradas é de:')
for m in galera:
    if m['sexo'] in 'ff':
        print() #print(f'{m['nome']}', end=)