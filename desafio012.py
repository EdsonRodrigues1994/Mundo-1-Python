#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de cesconto.

produto = float(input("Digite o valor do produto: "))
porcentagem =  5.00
desconto = produto - ((produto * porcentagem) / 100)

print("O valor do produto é R$ {:.2f} reais , com 5% de desconto o valor fica em R$ {:.2f} reais.".format(produto, desconto))