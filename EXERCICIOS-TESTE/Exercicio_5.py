"""
EXERCÍCIO 5 — Sistema de Transportes

Crie uma classe base chamada Transporte.

Essa classe deve possuir o método:
mover()

Depois crie quatro classes filhas:

- Carro
- Aviao
- Barco
- Trem

Cada classe deve sobrescrever o método mover()
mostrando uma ação diferente.

Exemplo esperado:

Carro está dirigindo
Avião está voando
Barco está navegando
Trem está andando nos trilhos

Crie uma lista com diferentes transportes
e percorra essa lista chamando mover() para cada um.
"""

class Transporte:
    def mover(self):
        raise NotImplementedError


class Carro(Transporte):
    def mover(self):
        print("Carro está dirigindo")


class Aviao(Transporte):
    def mover(self):
        print("Avião está voando")


class Barco(Transporte):
    def mover(self):
        print("Barco está navegando")


class Trem(Transporte):
    def mover(self):
        print("Trem está andando nos trilhos")


transportes = [
    Carro(),
    Aviao(),
    Barco(),
    Trem()
]

for transporte in transportes:
    transporte.mover()