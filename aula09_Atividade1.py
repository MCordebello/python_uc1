vet_dados=[15,3,2,94,3,5,3,36]
vetor=[15,2,3,94,3,52,3,36]

def criar_imprimir_lista ():
    vetor = [10, 20, 30, 40, 50]
    print(f"\n\t O conteúdo do vetor é: {vetor}\n")

def criar_imprimir_lista_v2 (vetor):
    print (f"\n\t O conteúdo do vetor é {vetor}")
    

def soma_dos_vetores (vetor):
    soma=sum(vetor)
    print(f"\n\t A soma dos vetores é {soma}\n")

def soma_dos_vetores_v2 (vetor):
    print(f"\n\t A soma dos vetores é {soma}\n")

def imprimir_elemento (vetor):
    for elemento in vetor:
        print("Elemento:", elemento)

def maior_e_menor (vetor):
    maior = max (vetor)
    menor = min (vetor)
    print(f"\n\t Maior valor é {maior}")
    print(f"\n\t Menor valor é {menor}")

def vetor_invertido (vetor):
    invertido = vetor[::-1]
    print(f"\n\tO inverso dos vetores é {invertido}")


def multiplicador (vetor):
    for elemento in vetor:
        mult=elemento*2
        print (f"\n\t A multiplicação é {mult}")  

def contar_elementos (vetor):
    ocorrencias=vetor.count(3)
    print (f"\n\t O valor 3 aparece {ocorrencias} vezes")

def vetor_crescente (vetor):
    vetor_ordenado = sorted(vetor)
    print(f"\n\t A ordem crescente é {vetor_ordenado}")

def remover_elementos (vetor):
    vetor_sem_duplicatas = list(dict.fromkeys(vetor))
    print(f"\n\t Vetor sem duplicatas é {vetor_sem_duplicatas}")

def par_ou_impar (vetor):
    par=[num for num in vetor if num % 2 == 0]
    impar=[num for num in vetor if num % 2 != 0]
    print(f"\n\t Os números pares são {par}")
    print(f"\n\t Os números impares são {impar} ")

def media_dos_elementos (vetor):
    media = sum(vetor) / len(vetor)
    acima_media = [num for num in vetor if num > media]
    print (f"/n/t A média é {media}")
    print (f"/n/t Elementos acima da média são {acima_media}")

if __name__ == "__main__" :

   #criar_imprimir_lista_v2 (vet_dados)

   #soma_dos_vetores  (vetor)
   #soma_dos_vetores (vet_dados)

   # imprimir_elemento (vet_dados)

   # maior_e_menor (vetor)
   #maior_e_menor (vet_dados)

   #vetor_invertido (vetor)
    #vetor_invertido (vet_dados)

   #multiplicador (vetor)
   #multiplicador (vet_dados)

   #contar_elementos (vetor)
   #contar_elementos (vet_dados)

  # remover_elementos (vetor)
  # remover_elementos (vet_dados)

  #par_ou_impar (vetor)
  #par_ou_impar (vet_dados)

  #vetor_crescente (vetor)
  #vetor_crescente (vet_dados)

  media_dos_elementos (vetor)
  media_dos_elementos (vet_dados)