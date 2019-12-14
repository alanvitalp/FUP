vetor1 = input()
vetor2 = input()

#Transformar a entrada numa lista de strings e depois converter em inteiro
vetor1 = [int(i) for i in vetor1.split(',')]
vetor2 = [int(i) for i in vetor2.split(',')]

if len(vetor1) == len(vetor2):
  resultado = 0
  tam = len(vetor1)
  matriz = []
  
  for i in range(tam):
    linha = []
    for j in range(tam):
      linha.append(0)
    matriz.append(linha)
  
  

  print ("Primeiro vetor:" ,vetor1)
  print ("Segundo vetor:" ,vetor2)
  
  for i in range(tam):
    resultado += vetor1[i] * vetor2[i]
  
  print ("Produto interno:" , resultado)
  
  for k in range(tam):
    for l in range(tam):
      matriz[k][l] = int(vetor1[k]) * int(vetor2[l])
  
  print ("Produto externo:")
  
  for i in range(tam):
    print(matriz[i])
  
  print("Produto externo transposto:")
  
  for k in range(tam):
    for l in range(tam):
      matriz[l][k] = int(vetor1[k]) * int(vetor2[l])
  
  for i in range(tam):
    print(matriz[i])

  
    
else:
  print ("Os vetores devem ter o mesmo número de elementos!")