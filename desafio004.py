# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele

n = input("Digite algo:")

# alnum = se o dado é ALFANUMÉRICO
print("É alfanúmerico?", n.isalnum())

#alpha = se o dado é uma string
print("É uma string?", n.isalpha())

#numeric = se o dado é numérico
print("É númérico?", n.isnumeric())

#upper = se o dado é todo maíusculo
print("É todo maiúsculo", n.isupper())

#lower = se o dado é todo minúsculo
print("É todo minúsculo", n.islower())