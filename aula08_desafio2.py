import sys
# def main(argumentos):
#     for arg in argumentos:
#          print(argumentos)

def calculadora (n1,n2,op):
    #print(f"{n1} {op} {n2}") 

    if op=="+":
        resultado=n1+n2
        return resultado
    elif op=="-":
        resultado=n1-n2
        return resultado
    elif op=="*":
        resultado=n1*n2
        return resultado
    elif op=="/":
        resultado=n1/n2
        return resultado
    
if __name__== "__main__":

    argumentos=sys.argv[1:]
    numero1=float(argumentos[0])
    operacao=argumentos[1]
    numero2=float(argumentos[2])
    
    print(calculadora(numero1,numero2,operacao))