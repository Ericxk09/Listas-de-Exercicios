numero = int(input("Numero: "))
n = 0
n1 = 2
n2 = []
while numero > 0 and n < numero:
     primo = numero//n1
     n2.append (primo * n1)
     if primo != 1 and n2[n] == numero:
        print("Não é primo")
        break
    
     elif numero//n1 == 1:
        print("Numero primo!")
        break
     n1 = n1 + 1
     n = n + 1
    
    
