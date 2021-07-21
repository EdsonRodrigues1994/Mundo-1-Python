#Crie um programa que leia o nome completo de ujma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúysculas
#Quantas letras ao todo(sem consideras os espaços)
#Quantas letras tem o primeiro nome


nome = str(input("Digite seu nome: ")).strip()
nomenovo = nome.split()

print("Nome maiúsculo: ", nome.upper())
print("Nome minúsculo: ", nome.lower())
print("Caracteres no nome desconsiderando os espaços: ", len(nome.replace(" ", "")))
print("Caracteres do primeiro nome:", len(nomenovo[0]))
