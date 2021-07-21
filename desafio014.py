#Escreva um programa que converta uma temperatura digitada em ºC e converta paa ºF

celsius = float(input("Digite a temperatura em ºC: "))
fh = celsius * 1.8 + 32
print("A temperatura em ºC é {}, e a temperatura convertida em ºF é {}.".format(celsius, fh))
