idade=int(input("Qual a sua idade?"))

if(idade>=18) or (pais=="s") and (banido=="n"):
    print("Autorizada a entrada")
else:
    print("Está de fora da festa")
    
banido=input("Está na lista de banidos? <s/n>").lower
pais=input("Está acompanhado dos pais? <s/n>").lower

