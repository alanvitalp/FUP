
custo_total = float(input("Digite o custo total da sua viagem: "))
valor_inicial = float(input("Digite o valor inicial: "))
valor_mensal = float(input("Digite o valor mensal à ser poupado: "))
rendimento_mensal = float(input("Digite o rendimento mensal(em %): "))

rendimento_mensal= (rendimento_mensal/100)

arrecadado = valor_inicial


meses = 0 

while (arrecadado <= custo_total):
  arrecadado +=  valor_mensal + (arrecadado*rendimento_mensal)
  meses += 1

print (f"Em {meses} meses você terá R${arrecadado:.2f} para sua viagem!")

