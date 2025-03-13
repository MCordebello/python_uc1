SENHA_CORRETA="6321"

idade=int(input("Qual é a sua idade? "))
senha=input("Qual é a senha?    ").lower()


if idade>=18:
    if senha==SENHA_CORRETA:
      print("Acesso liberado")
    else:
        print("Acesso bloqueado")
else:
    print("Idade invalida")



