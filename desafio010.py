#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

reais = float(input("Quantos reais você tem na carteira?"))
dolar = reais / 3.27

if(reais >= 3.27):
    print("Você pode comprar US$ {:.2f} dólar(es) com R${} reais.".format(dolar, reais))
else:
    print("Você não tem dinheiro suficiente para converter em no mínimo US$ 1 dólar.")