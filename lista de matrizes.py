def cria_matriz_identidade(ordem):
  # Cria matriz de zeros
  matriz_identidade = [[0 for x in range(ordem)] for y in range(ordem)]

  # Preenche a diagonal com 1
  for i in range(ordem):
    matriz_identidade[i][i] = 1
  
  
  return matriz_identidade
 
def mult_matriz_escalar(mat, escalar):
  
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      mat[i][j] = mat[i][j]*escalar
  
  return mat

def cria_lista_matrizes(ordem, numeros):
  lista = []
  
  for i in range(len(numeros)):
    mat = cria_matriz_identidade(ordem)
    matriz = mult_matriz_escalar(mat, numeros[i])
    lista.append(matriz)
  
  return lista
  

def mostra_matriz(mat):
  for linha in matriz:
    print(linha)


def mostra_lista_matrizes(lista_mat):
    mat = cria_lista_matrizes(ordem, numeros)
    
    for i in range(len(mat)):
      print (f"Matriz na posição {i}:")
      for j in range(ordem):
        print (mat[i][j])



ordem = int(input("Digite a ordem da matriz identidade: "))
numeros = input("Digite alguns números inteiros:")
numeros = [int(i) for i in numeros.replace(" ", "").split(',')]

mostra_lista_matrizes(cria_lista_matrizes(ordem, numeros))
  
  