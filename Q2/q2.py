def fibo(num):
    vet = [0, 1]
    while vet[-1] < num:
        prox = vet[-1] + vet[-2]
        vet.append(prox)
    return vet

def isFibo(num):   
    seq = fibo(num)
    return num in seq


numero = 22

vetorFibo = fibo(numero)

print(vetorFibo)
if isFibo(numero):
    print(numero,"está na sequência de fibonacci")  
else:
    print(numero,"não está na sequência de fibonacci")         
           