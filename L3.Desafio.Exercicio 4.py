numero = int(input("Digite um numero:" ))

n = 2 ## divisora
n1 = 2 ##contadora de primos
primo = [] ## armazena
saldo_fat = numero
k = k1 = 0
n_fat = []##numero fatoração

while saldo_fat != 1:
    if (n1 != n and (n1%n) == 0):##não primo
        n1 = n1 + 1
        n = 2
        
    elif n == n1:##primo e fatoração
        n1 = n1 + 1 
        primo.append(n)
        while primo[k] <= saldo_fat:
                if saldo_fat%primo[k] == 0:
                    saldo_fat = saldo_fat/primo[k]
                    n_fat.append(primo[k])
                    
                    k1 = k1 + 1
            
                elif saldo_fat%primo[k] != 0:
                    break
                    
                elif saldo_fat == 1:
                    print("Numero Primo!")
                    print("FATOR: ", numero,"^^1",)
                    break
        if n_fat.count(primo[k]) != 0:
            print(primo[k],"^^",n_fat.count(primo[k]))
                       
        n = 2
        k = k + 1 
        
    else:##não primo
        n = n + 1
