#Escreva um programa que leia um valor em metros e o exiba convertido em cenímetros e milímetros

metros = float(input("Metros?"))
centimetro = metros * 100
milimetro = metros * 1000

print("Você selecionou {} metros, que são equivalentes a {} centimetros e {} milimetros.".format(metros, centimetro, milimetro))
