numero = int(input("Digite um numero: "))

if numero > 0:
    invertido = str(numero)
    print("Numero: ",numero)
    print("Invertido: ",invertido[::-1])
else:
    print("Numero invalido")
