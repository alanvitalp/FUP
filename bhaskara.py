import math

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = float(b**2 - (4*a*c))

raiz = 0

if delta < 0:
    print ("A equação não possui raízes reais.")

else:
  raiz = math.sqrt(delta)
  
  if (raiz > 0) or (raiz == 0):
     x1 = (-b + raiz) / (2*a)
     x2 = (-b - raiz) / (2*a)
  
  if x1 == x2:
    print ("A equação possui 1 raiz real:")
    print (f"x = {x1}")
  
  if x1 != x2:
    print ("A equação possui 2 raízes reais:")
    print (f"x = {x1}")
    print (f"x = {x2}")
    
    