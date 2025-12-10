class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def andar(self):
        print("Anda!")

class Carro(Veiculo):
    pass

class Barco(Veiculo):
    def andar(self):
        print("Veleja!")

class Aviao(Veiculo):
    def andar(self):
        print("Voa!")

carro = Carro("Nissan", "Tiida")

print(carro.marca)
print(carro.modelo)
carro.andar()