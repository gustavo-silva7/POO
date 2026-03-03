class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade: {self.velocidade} km/h")
        print("-" * 20)


carros = []  # lista para armazenar objetos

while True:
    print("\nCriar novo carro")
    marca = input("Marca (ou 'sair'): ")

    if marca.lower() == "sair":
        break

    modelo = input("Modelo: ")

    while True:
        try:
            ano = int(input("Ano: "))
            break
        except ValueError:
            print("Ano inválido. Digite um número.")

    novo_carro = Carro(marca, modelo, ano)
    carros.append(novo_carro)

print("\nCarros cadastrados:")
for carro in carros:
    carro.exibir_informacoes()