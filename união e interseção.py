def interseção(vetor1, vetor2):
    intersec = []
    for num in vetor1:
      for num2 in vetor2:
        if num2 == num:
          intersec.append(num)
    return intersec

# número de elementos da lista
n = int(input("Qual número de elementos das listas?"))

# Declarando variáveis
vetor1 = []
vetor2 = []
união  = []

#Criando laços para percorrer os vetores
for i in range(0, n):
  num = int(input(f"Digite o elemento {i} do vetor 1 "))
  vetor1.append(num)
  
for i in range(0, n):
  num2 = int(input(f"Digite o elemento {i} do vetor 2 "))
  vetor2.append(num2)


#formatando as saídas
print ("Primeiro vetor:")
print (vetor1)
print ("Segundo vetor:")
print (vetor2)


união = (vetor1 + vetor2)

n_vetor1 = list(set(vetor1))
n_vetor2 = list(set(vetor2))

união = list(set(união))

print ("Vetor interseção:")
print (interseção(vetor1, vetor2))
print ("Vetor união:")
print (união)