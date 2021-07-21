#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
#necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
area = largura * altura
tinta = area / 2.0

print("A largura informada é {} metros, a altura informada é {} metros, e a área é {}m², serão utilizadas {} latas de tinta para pintar o ambiente.".format(largura, altura, area, tinta))