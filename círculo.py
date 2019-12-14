import math


def criaPonto():
  valorX = float(input(""))
  valorY = float(input(""))
  
  return {'x':valorX, 'y':valorY}
  



def calculaDistancia(ponto1, ponto2):
  dist =  math.sqrt((ponto1['x'] - ponto2['x'])**2 + (ponto1['y'] - ponto2['y'])**2)
  
  return dist


def criaCirculo():
  pontoCentro = criaPonto()
  valorRaio =  criaPonto()
  
  return {'centro':pontoCentro, 'raio':valorRaio}


def calculaComprimento(Raio):
  c = 2*math.pi*Raio
  
  return c



circulo = criaCirculo()
Raio = calculaDistancia(circulo['centro'],circulo['raio'])
comprimento = calculaComprimento(Raio)


print (f"Centro do círculo: {circulo['centro']['x']} {circulo['centro']['y']}")
print (f"Ponto no círculo: {circulo['raio']['x']:.1f} {circulo['raio']['y']:.1f}")
print (f"Raio do círculo: {Raio:.4e}")
print (f"Comprimento do círculo: {comprimento:.4e}")



