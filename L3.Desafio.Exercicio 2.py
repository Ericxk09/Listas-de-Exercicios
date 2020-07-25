conta_pagar = int(input("Conta a Pagar: "))
valor_pgt = int(input("Valor Pagamento: "))

saldo_troco = valor_pgt - conta_pagar
notas = []
notas.append(50)
notas.append(20)
notas.append(10)
notas.append(5)
notas.append(2)
notas.append(1)
nro_notas = []
n = 0

while saldo_troco > 0:
    nro_notas.append(int(saldo_troco // notas[n]))
    saldo_troco = saldo_troco % notas[n]
    n = n + 1
    n1 = n
n = 0    
while saldo_troco == 0 and n < n1:
    saldo_troco = valor_pgt - conta_pagar
    if nro_notas[n] > 0:
        print("Troco: $",saldo_troco)
        print(nro_notas[n],"Notas de ",notas[n])        
    n = n + 1
