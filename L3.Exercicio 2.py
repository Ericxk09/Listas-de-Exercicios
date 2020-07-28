print("Cadastre seu usuario e senha")
usuario = input("Usuario: ")
senha = input("Senha: ")

while usuario == senha:
    print("Usuario e senha não podem ser iguais!")
    print("Tente Novamente")
    print("") ##usado apenas para saltar a linha
    usuario = input("Usuario: ")
    senha = input("Senha: ")
print("Cadastrado com sucesso!")    
