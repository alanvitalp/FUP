soma = 0
divisores = 0 

for número in range(1,10000):
    soma = 0
    
    for div in range(1,round(número/2)+1):
        if número % div == 0:
            soma += div
    
    if soma == número:
        divisores += 1
        print(f"{número} é um número perfeito!")
    
    if divisores == 4:
        break