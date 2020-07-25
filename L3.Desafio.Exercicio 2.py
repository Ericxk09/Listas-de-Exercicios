conta_pagar = int(input("Conta a Pagar: "))
valor_pgt = int(input("Valor Pagamento: "))

saldo_troco = valor_pgt - conta_pagar
notas = [50,20,10,5,2,1]
nro_notas = []
n = 0

while saldo_troco > 0:
    nro_notas.append(int(saldo_troco // notas[n]))
    saldo_troco = saldo_troco % notas[n]
    n = n + 1

n1 = n    
n = 0
print("Troco: $",valor_pgt - conta_pagar)

while saldo_troco == 0 and n < n1:
    if nro_notas[n] > 0:
        print(nro_notas[n],"Notas de ",notas[n])        
    n = n + 1

