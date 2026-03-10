# EXERCÍCIO 2 – Sistema de Veículos
# Crie uma classe chamada Veiculo com:
# Atributos:
# ● marca
# ● modelo
# Método:
# ● exibir_info()
# Mensagem:
# Veículo: marca - modelo
# Crie duas classes filhas:
# ● Carro
# ● Moto
# Regras
# A classe Carro deve ter:
# ● atributo: portas
# A classe Moto deve ter:
# ● atributo: cilindradas
# Crie objetos e mostre suas informações

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, porta):
        super().__init__(marca, modelo)
        self.porta = porta

    def portas(self):
        print(f"Quantidade de portas: {self.porta}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
       super().__init__(marca, modelo)  
       self.cilindradas = cilindradas

    def cilindrada(self):
        print(f"Cilindradas: {self.cilindradas}")


veiculos = []
print("=========================")
print("==== TIPO DE VEICULO ====")
print("-- Para MOTO : digite M--")
print("-- Para CARRO: digite C--")
print("=========================")

while True:
    tipo_veiculo = input("Qual tipo de veiculo (DIGITE 'S' PARA SAIR): ").strip().lower()

    if tipo_veiculo in ['m','c']:
        marca = input("Marca: ")
        modelo = input("Modelo: ")

    elif tipo_veiculo == 's':
        break

    else:
        print("INFORMAÇÃO INVALIDA!")
        continue

    if tipo_veiculo == 'm':
        cilindradas = input("Cilindradas: ")
        veiculos.append(Moto(marca,modelo,cilindradas))

    elif tipo_veiculo == 'c':
        portas = input("Qunatidade de portas: ")
        veiculos.append(Carro(marca, modelo, portas))

for veiculo in veiculos:
    veiculo.exibir_info()

    if isinstance(veiculo, Moto):
        veiculo.cilindrada()

    elif isinstance(veiculo,Carro):
        veiculo.portas()