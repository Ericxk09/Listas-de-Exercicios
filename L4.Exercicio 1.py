import random

numeros = random.sample(range(100),10)
maior =  menor = numeros[0]
for x in numeros[1:]:
    if x > maior:
        maior = x
    elif x < menor:
        menor = x

print("Lista :",numeros)
print("Maior :",maior)
print("Menor :",menor)

