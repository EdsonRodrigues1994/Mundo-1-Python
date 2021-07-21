#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro
#custa R60 por dia e RS0,15 por KM rodado.

km = float(input("Qual a quantidade de km percorridos? "))
dias = int(input("Quantos dias o carro foi alugado? "))

total = (dias * 60) + (km * 0.15)
print("O carro percorreu {} km em {} dias de aluguel. O total a ser pago é: R$ {:.2f} reais.".format(km, dias, total))