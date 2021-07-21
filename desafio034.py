#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Parasalários superiores a R$1.250,00, calculke um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input("Digite o seu salário: "))


if salario > 1250.0:
    aumento = salario * 10 / 100
    print("O seu salário atual é R${:.2f}, com o aumento de 10% convertidos em R${:.2f}, passará a ser R${:.2f}.".format(salario, aumento, aumento + salario))
else:
    aumento = salario * 15 / 100
    print("O seu salário atual é R${:.2f}, com o aumento de 15% convertidos em R$ {:.2f}, passará a ser R${:.2f}.".format(salario, aumento, aumento + salario))