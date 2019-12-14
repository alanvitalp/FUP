nome = str(input("digite o seu nome "))
peso = float(input("digite o seu peso "))
altura = float(input("digite a sua altura "))

imc = (peso/(altura*altura))

print (f"O IMC de {nome} é: {imc}")
