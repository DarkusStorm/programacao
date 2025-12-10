class Pessoa:
    def __init__(self, n):
        self.nome = n

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}.")


pessoa1 = Pessoa("Arthur")
pessoa2 = Pessoa("Heitor")

pessoa1.cumprimentar()
