# input de String
# Conversões

matriz = input("")
matriz = matriz.split(';')

matriz1 = []
# Criando matriz
mat1 = []

for i in range(len(matriz)):
  coisa = matriz[i].strip(" ").split(' ')
  mat1.append([])
  for j in range(len(coisa)):
    try:
      mat1[i].append(int(coisa[j]))
    except ValueError:
      mat1[i].append(float(coisa[j]))
      
def cria_dicionario_matriz(mat1):
  
  for item in matriz:
    matriz1.append([float(número) for número in item.strip(' ').split(' ')])
  

  # Dimensão
  
  dim = []
  dim.append(len(mat1))
  dim.append(len(mat1[0]))
 
  # Traço da matriz
  traco = 0
  for i in range(len(mat1)):
    traco += mat1[i][i]
    
  # É quadrada?
  
  if dim[0] == dim[1]:
    dic = {'matriz': matriz1, 'dimensões': dim, 'quadrada': True, 'traço': float(traco)}
  
  else:
    dic = {'matriz': matriz1, 'dimensões': dim, 'quadrada': False}
  
  return dic

traco = 0

# Traço fora do loop
for i in range(len(mat1)):
    traco += mat1[i][i]
traço = float(traco)

#Dimensão fora do loop

dim = []
dim.append(len(mat1))
dim.append(len(mat1[0]))

#Chamando as funções

dicionario_matriz =  cria_dicionario_matriz(mat1)



def mostra_dicionario_matriz(dicionario_matriz):
  
  print(f"Dicionário original: {dicionario_matriz:}")
  print("Dicionário formatado:")
  print ("Matriz:")
 
  for item in matriz1:
    print (item)
  print(f"Dimensões: {dim}")

  
  if dim[0] == dim[1]:
    print ("A matriz é quadrada!")
    print (f"Traço: {traço}")
  
  else:
    print ("A matriz não é quadrada!")

mostra_dicionario_matriz(dicionario_matriz)