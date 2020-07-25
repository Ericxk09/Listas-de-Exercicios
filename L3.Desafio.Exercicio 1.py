n = 1
print("Digite zero ou um valor menor que 0 para parar o programa")

while n >= 1:
    
    n = int(input("Digite um numero: "))
    a = 1
    b = a + 1
    c = b + 1
    x = a * b * c

    while x != n or x == n:
        if x > n and n >= 1:
            print("Numero não é triangular")
            print("Digite zero ou um valor menor que 0 para parar o programa")
            print()
            break
        elif x == n:
            print('A: ',a)
            print("B: ",b)
            print("C: ",c)
            print(f"A({a}) * B({b})* C({c}) = ", x)
            print("Numero Triangular")
            break
        elif n <= 0:
            print("Loop encerrado!")
            break
        a = a + 1
        b = a + 1
        c = b + 1
        x = a * b * c
            
