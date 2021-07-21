#Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno, cosseo e tangente desse ângulo.
import math
angulo = float(input("Digite o angulo: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O ângulo digita foi foi {}, que corresponde ao seno {:.2f}, ao cosseno {:.2f} e a tangente {:.2f}.".format(angulo, seno, cosseno, tangente))

