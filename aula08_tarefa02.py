def apresentar(nome, idade):
    print(f"Nome:{nome}, Idade:{idade}")
apresentar ("Alice", 30) #posicional
apresentar (idade=30, nome="Alice") #Nomeado
    
def saudacao(nome="Mundo"):
 print(f"Olá, {nome}!")
saudacao() # Saída: Olá, Mundo!
saudacao("Alice") # Saída: Olá, Alice!  

def listar_nomes(*nomes):
   for nome in nomes:
      print(nome)
listar_nomes("Alice", "2", "Charlie")

def saudacao():
   print("Olá do módulo!")
if __name__=="__main__":
    saudacao()
