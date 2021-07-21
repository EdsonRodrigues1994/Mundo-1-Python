#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input("Digite sua cidade: ")
nomecid = cidade.title().split()

print(nomecid)

if nomecid[0] == "Santo":
    print("Sua cidade começa com Santo")
else:
    print("Sua cidade não começa com SANTO")