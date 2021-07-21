# Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário
# tebtar descobrir qualk foi o número escolhido pelo computador.

import random
from time import sleep

sorteio = random.randint(0, 5)
chute = int(input("Digite um número de 0 a 5: "))
print("Processando ...")
sleep(2)

if chute == sorteio:
    print("Você acertou!")
else:
    print("Eu pensei no número {}, você perdeu!".format(sorteio))
