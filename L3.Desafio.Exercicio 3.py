numero = int(input("Numero: "))
n = 0
n1 = [2,3,4,5,6,7]
n2 = []
while numero > 0 and n < 6:
     primo = numero//n1[n]
     n2.append (primo * n1[n])
     if primo != 1 and n2[n] == numero:
        print("Não é primo")
        break
    
     elif numero//n1[n] == 1:
        print("Numero primo!")
        break
    
     n = n + 1
if n == 6:
    print("Numero primo!")
    
    
