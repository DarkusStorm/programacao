class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def imprimirNome(self):
        print(self.nome, self.sobrenome)


pessoa1 = Pessoa("João", "Roccella")

pessoa1.imprimirNome()


class Aluno(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.nome = nome
        self.sobrenome = sobrenome
        self.anoDeConclusao = 2026


aluno1 = Aluno("Pedro Cesar", "Oliveira")

aluno1.imprimirNome()
print(aluno1.anoDeConclusao)
