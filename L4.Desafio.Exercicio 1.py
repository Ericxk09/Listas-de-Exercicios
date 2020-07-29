import random

numeros = random.sample(range(100),10)
k = 0
n = 0
while k < 10:
    if n > numeros[k]:
        k = k + 1
    else:
        n = numeros[k]
        k = k + 1
print(numeros)
print(n)
