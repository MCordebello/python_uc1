nome=input("Crie seu nome com mais de três letras: ")
senha=input("Crie uma senha com seis ou mais caracteres: ")

if (len (nome)>3):
    print("Seu usuário é válido!")
elif (len (senha)<6):
    print("Crie um usuário com mais de três caracteres")
elif (senha=="123456") or (senha=="senha"): 
    print( "Senha fraca")
else:
    print(" Cadastro liberado)")


