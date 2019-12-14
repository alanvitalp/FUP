string = str(input("Digite o número identificador: "))
vetor = []


print (f"Número identificador: \"{string}\"")

for i in range(0, 8):
  num = string[i]
  vetor.append(ord(num))

soma = sum(vetor)

print ("Soma dos caracteres ASCII:", end=" ")

for i in range(0, len(vetor)):
  
  if i == len(vetor)-1:
    print (vetor[i], end=" =")
    print ("", soma)
  
  else:
    print (vetor[i], end="+")

soma1 = str(soma)    

print (f"Conversão: {soma} -> \"{soma}\"")
print (f"Resultado final: \"{string}-{soma}\"")