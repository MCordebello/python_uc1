class Livro:

    def __init__ (self, titulo, autor, ano):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano
        self.emprestado=True

    def exibir_info(self):
        if self.emprestado==True:
            status="disponivel"
        else:
            status="emprestado"
        print(f"{self.titulo} {self.autor} ({self.ano}) está {status}")

class Biblioteca:

    def Adicionar():
        pass
    def Listar():
        pass
    def emprestar(self):
        self.emprestado=True
    def devolver(self):
        self.emprestado=False
        
    
        
    



