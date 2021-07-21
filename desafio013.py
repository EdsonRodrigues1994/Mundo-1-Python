#Escreva um programa que adicione uma porcentagem no salario de um funcionario e traga na tela.


salario = float(input("Digite seu salário:"))
porcentagem = 15.00
aumento = salario + ((salario * porcentagem ) / 100)

print("O seu salário é R$ {:.2f} reais, com 15% de aumento fica em R$ {:.2f} reais.".format(salario, aumento))


