n1 =  int(input("Numero 1: "))
n2 =  int(input("Numero 2: "))

while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
    print(n2)
