# Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

sair = 0

while sair == 0:
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
        ''')
    opcao = input('Digite uma das opções: ')
    if opcao == '1':
        soma = num1 + num2
        print('A soma desses números é de: ', soma)
    elif opcao == '2':
        mult = num1 * num2
        print('A multiplicação entre esses números é de: ', mult)
    elif opcao == '3':
        if num1 <= num2:
            print(f'{num2} é maior')
        elif num1 == num2:
            print('São iguais')
        else:
            print(f'{num1} é maior')
    elif opcao == '4':
        continue
    elif opcao == '5':
        print('TCHAU')
        sair += 5
        continue
    else:
        print('Opção inválida')