#idade<=21 anos

idade=int(input("Digite a sua idade: "))
renda=float(input("Digite a sua renda : "))
cadastro=(input("Está incluso no serasa <s/n>")).lower()

if(idade>=21) and (renda>2000) and (cadastro=="n"):
    print("Empréstimo aprovado")
else:
    print("Empréstimo reprovado")


