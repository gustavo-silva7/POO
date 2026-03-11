"""
EXERCÍCIO 4 — Sistema de Impostos

Crie uma classe base chamada Imposto.

Essa classe deve possuir o método:
calcular(valor)

Depois crie três classes filhas:

- ICMS
- ISS
- IPI

Cada classe deve calcular o imposto usando
uma porcentagem diferente.

Exemplo:

Valor: 100

ICMS: 18
ISS: 5
IPI: 10

Crie uma lista com diferentes impostos e execute o cálculo
para o mesmo valor utilizando polimorfismo.
"""

class Imposto:
    def calcular(self,valor):
        raise NotImplementedError
    
class ICMS(Imposto):
    def calcular(self, valor):
        imposto = valor * 0.18
        print(f"ICMS: {imposto}")

class ISS(Imposto):
    def calcular(self, valor):
        imposto = valor * 0.05
        print(f"ISS: {imposto}")

class IPI(Imposto):
    def calcular(self, valor):
        imposto = valor * 0.10
        print(f"IPI: {imposto}")

valor = int(input("Valor: "))

impostos = [ICMS(), ISS(), IPI()]

for i in impostos:
    i.calcular(valor)