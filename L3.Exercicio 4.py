numero = int(input("Digite um numero: "))
a,b = 1, 1
n = 1

while n <= numero - 2:
    a, b = b, a + b
    n = n + 1
    
print("b:", b)
