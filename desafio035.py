#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

n1 = float(input("Digite a primeira reta:"))
n2 = float(input("Digite a segunda reta: "))
n3 = float(input("Digite a terceira reta: "))
soma = n1 + n2

if soma > n3:
    print("Você pode formar um triângulo!")
else:
    print("Você não pode formar um triângulo!")