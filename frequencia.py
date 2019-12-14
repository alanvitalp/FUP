def monta_dicionario_palavras(texto):
  dic_palavras = {}
 
  for palavra in tex:
    
    if palavra in dic_palavras:
      dic_palavras[palavra] += 1
   
    if palavra not in dic_palavras:  
      dic_palavras[palavra] = 1
 
 return dic_palavras


def mostra_dicionario_palavras(dic_palavras):
  
  print ("Frequência de palavras:")
  
  for palavra in dic_palavras:
    pal = palavra.strip(".!,")
    print (f"{pal}: {dic_palavras[palavra]}x")
  
  
def monta_dicionario_caracteres(dic_palavras):
  dic_caracteres = {}
  
  for caractere in texto1:
    
    if caractere in dic_caracteres:
      dic_caracteres[caractere] += 1
    
    if caractere not in dic_caracteres:  
      dic_caracteres[caractere] = 1
  
  return dic_caracteres

def mostra_dicionario_caracteres(dic_caracteres):
  print ("Frequência de caracteres:")
  
  for isso in dic_caracteres:
    print (f"{isso}: {dic_caracteres[isso]}x")


texto = input("")
tex = texto.lower().strip(".!,").split()
tex1 = texto.lower()
texto1 = list(tex1)

  

dic_palavras = monta_dicionario_palavras(tex.sort())
mostra_dicionario_palavras(dic_palavras)

dic_caracteres = monta_dicionario_caracteres(texto1.sort())
mostra_dicionario_caracteres(dic_caracteres)