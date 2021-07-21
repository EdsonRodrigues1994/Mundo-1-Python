#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido

import random

nomes = ['Joao', 'Carla', 'Maria', 'Thais']

print(nomes[random.randrange(len(nomes))])

