#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
#apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
#Mostre também quantos valores pares foram digitados.

soma = 0
cont = 0

for a in range(1,7):
    num = int(input(f'Digite {a}° número: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'Você digitou {cont} números pares e sua soma foi {soma}')