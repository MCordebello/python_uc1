"""
pessoa = {"nome": "Ana", "idade": 30, "cidade": "Petrópolis"}
print(f"Dados da pessoa: {pessoa}")
pessoa["idade"]=38
print(f"Dados atualizados: {pessoa} ")
pessoa["email"]="ana@gmail.com"
print(f"Dados atualizados: {pessoa}")
del pessoa ["nome"]
del pessoa ["email"]
print(f"Dados atualizados: {pessoa}")
"""

'''
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
d3 = {**d1, **d2}
print("Resultado:", d1)'


d1 = {"a": 1, "b": 2}
d3= {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

print(f"Dicionários originais: ")
print(f"D1 :{d1}")
print(f"D2 :{d2}")

d1.update(d2)
d2.update(d3)

print(f"Dicionários atualizados: ")
print(f"D1 :{d1}")
print(f"D2 :{d2}")'

frase = "o rato roeu a roupa do rei de roma"
palavras = frase.split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)'

alunos = {}

alunos[1] = {"nome": "Maria", "notas": [7.5, 8.0, 9.2]}
alunos[2] = {"nome": "João", "notas": [6.0, 7.8, 8.5]}
alunos[3] = {"nome": "Carlos", "notas": [5.5, 6.5, 7.0]}

for id_aluno, info in alunos.items():
    notas = info["notas"]
    media = sum(notas) / len(notas)
    info["média"] = round(media, 2)

print(alunos)'
'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False 

    def exibir_info(self):
        if self.ligado==True:
            status="ligado"
        else: 
            status="desligado"
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}.") 

    def ligar (self):
        self.ligado = True

    def desligar (self):
        self.ligado = False   

if __name__ == "__main__" :
    print(f"Criando um objeto de classe carros")
    meu_carro = Carro ("Toyota", "Corolla", 2020)
       #print(meu_carro)
    meu_carro.ligar()
    meu_carro.exibir_info()
    
   
