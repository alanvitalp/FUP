tabela = []
time = []

numero_jogos = int(input("Foram quantos jogos?"))

for i in range(numero_jogos):
  entrada = input(f"Como foi o jogo {i+1}? (time1, time2, gols1, gols2): ")
  lista_entrada = entrada.replace(' ','').split(',')
  times = lista_entrada[:2]
  placar = [int(lista_entrada[i]) for i in range(2, 4)]
  tabela.append(times)
  tabela[i].append(placar)
  time.append(times)

print("Tabela de jogos lida:")

for jogo in tabela:
  print (jogo)

print ("Tabela de jogos formatada:")

for jogo in tabela:
  print (f"{jogo[0]} vs {jogo[1]}: {jogo[2][0]} x {jogo[2][1]}")

print("Times participantes:")

países = []

for jogo in tabela:
  países.append(jogo[0])
  países.append(jogo[1])

países = sorted(set(países))

print (', '.join(países))
  
mais_gols = tabela[0][2][0]
menos_gols = mais_gols
linha_mais = 0
time_mais = 0
linha_menos = 0
time_menos = 0

for x in range(len(tabela)):
  
  if tabela[x][2][0] > mais_gols:
      mais_gols = tabela[x][2][0]
      linha_mais = x
      time_mais = 0
    
 
  if tabela[x][2][1] > mais_gols:
      mais_gols = tabela[x][2][1]
      linha_mais = x
      time_mais = 1
  
  
  if tabela[x][2][0] < menos_gols:
      menos_gols = tabela[x][2][0]
      linha_menos = x
      time_menos = 0
  
  if tabela[x][2][1] < menos_gols:
      menos_gols = tabela[x][2][1]
      linha_menos = x
      time_menos = 1

print (f"Time com mais gols: {tabela[linha_mais][time_mais]}, com {mais_gols} gol(s).")
print (f"Time com menos gols: {tabela[linha_menos][time_menos]}, com {menos_gols} gol(s).")