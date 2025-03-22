"""
def saudacao():
    print("Olá, seja bem-vindo(a) ao curso de Python!")


if __name__=="__main__":
    saudacao()


def soma(a, b):
    return a + b

def testar_soma():
    resultado=soma(5,7)
    print("A soma é:", resultado)

if __name__ == "__main__":
    testar_soma()
"""

def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
def testar_fatorial():
    numero=int(input("\n\n\tInforme um número: "))
    resultado=fatorial(numero)
    
    print (f"\n\n\tFatorial de {numero} é igual a {resultado}\n\n")

if __name__ == "__main__":
    testar_fatorial()