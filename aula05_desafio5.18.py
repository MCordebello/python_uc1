# numero1=float(input("Digite o primeiro número: "))
# numero2=float(input("Digite o segundo número: "))
# numero3=float(input("Digite o terceiro número: "))

# if(numero1>numero2) and (numero1>numero3):
#     print("O primeiro número é o maior")
# elif(numero2>numero1) and (numero2>numero3):
#     print("O segundo número é o maior")
# else:
#     print("O terceiro número é o maior")


listnum= []
num = input("Diga um número")
listnum.append(num)
num = input("Diga um número")
listnum.append(num)
num = input("Diga um número")
listnum.append(num)

print(max(listnum))