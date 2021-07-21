#Faça um programa que leia três números e mostre quyal é o maior e qual é o menor.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número:"))

if n1 > n2 and n1 > n3:
    print("Os números digitados foram: {}, {} e {} e o número {} é o maior".format(n1, n2, n3, n1))
elif n2 > n1 and n2 > n2 > n3:
    print("Os números digitados foram: {}, {} e {} e o número {} é o maior número".format(n1, n2, n3, n2))
else:
    print("Os números digitados foram: {}, {} e {} e o número {} é o maior número".format(n1, n2, n3, n3))

if n1 < n2 and n1 < n3:
    print("Os números digitados foram: {}, {} e {} e o número {} é o menor número".format(n1, n2, n3, n1))
elif n2 < n1 and n2 < n3:
    print("Os números digitados foram: {}, {} e {} e o número {} é o menor número".format(n1, n2, n3, n2))
else:
    print("Os números digitados foram: {}, {} e {} e o número {} é o menor número".format(n1, n2, n3, n3))