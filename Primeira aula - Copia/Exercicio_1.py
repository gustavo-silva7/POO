# Definição da CLASSE
class Carro:

# Método construtor (responsável por criar o objeto)
    def __init__(self, marca, modelo, ano):

# ATRIBUTOS (características do objeto)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

#MÉTODO (ação/comportamento)
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro acelerou para {self.velocidade} km/h.")

#METODO
    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
            print(f"O carro reduziu para {self.velocidade} km/h.")

#METODO
    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade atual: {self.velocidade} km/h")
            
# INSTANCIAÇÃO (criação do objeto)
carro1 = Carro("Toyota", "Corolla", 2022)

# Outro objeto da mesma classe
carro2 = Carro("Honda", "Civic", 2023)


# UTILIZAÇÃO DOS MÉTODOS
carro1.acelerar(50)
carro1.frear(20)
carro1.exibir_informacoes()
print("------------------")
carro2.acelerar(80)
carro2.frear()
carro2.exibir_informacoes()    