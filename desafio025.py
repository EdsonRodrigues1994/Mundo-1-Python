#Crie um programa que verifique se existe a palavra "silva" no nome de uma pessoa:

nome = input("Digite seu nome: ")

if "Silva" in nome.title():
    print("Você possui Silva no nome")
else:
    print("Você não possui Silva no nome")

