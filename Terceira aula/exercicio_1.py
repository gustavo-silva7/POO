'''Parte 3 – Exercício Prático
Crie um programa em Python com:
Uma classe chamada Veiculo com um método:
mover()
Depois crie duas classes filhas:
Carro
Bicicleta
Cada uma deve sobrescrever o método mover().
Exemplo esperado:
O carro está andando
A bicicleta está pedalando'''

class Veiculo:
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print('O carro esta andando')


class Bike(Veiculo):
    def mover(self):
        print('A bicicleta esta pedalando')

veiculos = [Carro(), Bike()]

for i in veiculos:
    i.mover()

