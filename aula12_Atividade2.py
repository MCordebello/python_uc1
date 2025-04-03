"""class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

def fazer_barulho(animal):
        animal.fazer_som()

meu_cachorro = Cachorro()
meu_gato = Gato()

fazer_barulho(meu_cachorro)
fazer_barulho(meu_gato)"""

class Conta:
     def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

     

     def depositar (self,valor):
         self.saldo += valor
         print (f"Depósito de R${valor:.2f} realizado na conta {self.numero}")

     def sacar (self, valor):
         if valor > self.saldo:
             print("Saldo insuficiente para saque!")
         else:
             self.saldo-=valor
             print (f"Saque de R$ {valor:.2f} realizado na conta {self.numero}.")
     def exibir_dados(self):
        return f"Conta {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}"

     def __str__(self):
        return self.exibir_dados()