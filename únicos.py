n = int(input("Qual o número de elementos da lista? "))

lista = []
nova_lista = []

for i in range(0, n):
  num = int(input(f"Digite o elemento {i} da lista "))
  lista.append(num)

nova_lista = list(set(lista))

print ("Lista original:")
print (lista)
print ("Nova lista:")
print (nova_lista)