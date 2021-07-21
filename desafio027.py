#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguidao primeiro e o último nome separadamente.

nome = input("Digite seu nome: ")
nomenovo = nome.title().split()

print("O nome digitado foi {}, o seu primeiro nome é {}, e seu último nome é {}. ".format(nome.title(), nomenovo[0], nomenovo[-1]))