#série: 2, 7, 3, 4, 21, 12, 8, 63, 48, 16,189, 192, 32, 567, 768

antepenúltimo = 2
penúltimo = 7
último = 3

n = int(input(""))

if n == 1:
  soma = 2

if n == 2:
  soma = 9

if n >= 3:
  soma = 12

for i in range(4, n+1):
  if i % 3 == 1:
    antepenúltimo = antepenúltimo * 2
    soma += antepenúltimo
  
  if i % 3 == 2:
    penúltimo = penúltimo * 3
    soma += penúltimo
    
  
  if i % 3 == 0:
    último = último * 4
    soma += último

if n % 3 == 1:
  x = antepenúltimo

if n % 3 == 2:
  x = penúltimo

if n % 3 == 0:
  x = último

print (f"A posição {n} da série é igual a {x}.")
print (f"A soma dos {n} primeiros elementos da série é igual a {soma}.")