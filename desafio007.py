#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2

if ( media < 5):
    print("Sua média é {} e você foi reprovado.".format(media))
else:
    print("Sua média é {} e você foi aprovado.".format(media))

