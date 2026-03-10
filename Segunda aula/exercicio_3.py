"""EXERCÍCIO 3 – Sistema Bancário
Simples
Crie uma classe ContaBancaria
Atributos:
● titular
● saldo
Métodos:
● depositar()
● sacar()
Agora crie duas classes filhas:
● ContaCorrente
● ContaPoupanca
Regras
ContaCorrente:
● taxa de saque = 2 reais
ContaPoupanca:
● método render_juros()
"""

class ContaBancaria:
    def __init__(self,titular,saldo = 0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor <= 0:
            print("""VALOR INVALIDO!
                  ola
                  """)
            return
        
        self.saldo += valor
        print(f"Deposito de R$ {valor} realizado com sucesso!")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor
        print(f"Saque de {valor} realizado.")

    def mostrar_saldo(self):
        print(f"Saldo atual: {self.saldo}")

class ContaCorrente(ContaBancaria):

    taxa_saque = 2

    def sacar(self, valor):

        valor_total = valor + self.taxa_saque

        if valor_total > self.saldo:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor_total
        print(f"Saque de {valor} + taxa de {self.taxa_saque}")


class ContaPoupanca(ContaBancaria):

    def render_juros(self, taxa):

        juros = self.saldo * taxa
        self.saldo += juros

        print(f"Juros aplicados: {juros}")

conta1 = ContaCorrente("Carlos", 100)
conta2 = ContaPoupanca("Ana", 200)

conta1.depositar(50)
conta1.sacar(30)
conta1.mostrar_saldo()

conta2.render_juros(0.05)
conta2.mostrar_saldo()