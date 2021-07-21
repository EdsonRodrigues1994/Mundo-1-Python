#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = int(input("Informe a distancia da viagem em KM: "))


if distancia > 200:
    preco = 0.50 * distancia
    print("D distância da sua viagem é de {}KM e o valor a ser pago é R${:.2f}.".format(distancia, preco))
else:
    preco = 0.45 * distancia
    print("A distância da sua viagem é de {}KM e o valor a ser pago é R${:.2f}.".format(distancia, preco))