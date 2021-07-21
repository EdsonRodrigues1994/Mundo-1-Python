#Escreva um programa queleia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uyma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 ´pr cada km acima do limite

velocidade = int(input("Digite a velocidade doi carro: "))
multa = (velocidade - 80) * 7

if (velocidade > 80):
    print("Você foi multado por estar acima da velocidade permitida de 80k/h!")
    print("A sua velocidade atual é {}, serão cobrados R$7,00 por cada KM acima do permitido, totalizando em R${} reais em multa.".format(velocidade, multa))
else:
    print("Velocidade dentro do limite permitido para a via. Sua velocidade atual é {}KM/h".format(velocidade))