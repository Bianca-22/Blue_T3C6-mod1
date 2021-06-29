'''
02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
'''

#Ex: 02
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))

a = (n1,n2,n3,n4)
print(a)
print(f'O número 9 apareceu {a.count(9)}.')
print(f'O número 3 está na {a.index(3)}° posição.')