preço = 5.00
lucro = 0
despesa = 0

ingressos = int(input(""))
despesa = int(input(""))
a = int(input(""))

lucro = (ingressos*preço) - despesa

maior_lucro = lucro  # guarda o valor do maior lucro
qtd_lucro = ingressos + a # guarda a quantidade de ingressos do maior lucro
valor_lucro = preço  # guarda o valor do ingresso que traz o maior lucro

print ("Preço\tPúblico\tLucro")
print (f"R${preço:.2f}\t{ingressos}\tR${lucro}")

while preço > 1:
  ingressos = ingressos + a
  preço = preço - 0.5
  lucro = (ingressos*preço) - despesa
  
  if lucro > maior_lucro:
    maior_lucro = lucro
    qtd_lucro = ingressos
    valor_lucro = preço
  
  print(f"R${preço}\t{ingressos}\tR${lucro}")

print (f"Ao preço de R${valor_lucro:.2f} serão vendidos {qtd_lucro:.2f} ingressos e o lucro será de R${maior_lucro:.2f}.")