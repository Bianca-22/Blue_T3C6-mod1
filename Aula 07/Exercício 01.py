#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
#o maior e o menor peso lidos.


menor = maior = 0
for i in range(1,6):
    peso = float(input(f'Peso da {i}° pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior: ',maior)
print('Menor: ',menor)
