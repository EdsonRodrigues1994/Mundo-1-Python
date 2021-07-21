frase = str(input("Digite uma frase: ")).upper().strip()

print("A letra 'A' aparece {} vezes na frase.".format(frase.count("A")))

print("A letra 'A' aparece na primeira posição {}: ".format(frase.find("A")+1))

print("A letra 'A' aparece na última posição {}: ".format(frase.rfind("A")+1))




