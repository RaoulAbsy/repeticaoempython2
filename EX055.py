maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input("Quantos kg pesa a {}ª pessoa? ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("A pessoa mais leve registrada possui {}kg e a mais pesada tem {}kg.".format(menor, maior))