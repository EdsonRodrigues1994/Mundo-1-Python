#Crie um programa que leia um número real quqlauqer pelo teclado e mostre na tela a sua porç]ao inteira


import math
num = float(input("Digite um número flutuante: "))

print("O número digitado foi {}, e sua porção inteira é {}.".format(num, math.floor(num) ))