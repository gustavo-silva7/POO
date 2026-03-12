"""
DESAFIO — Sistema de Pagamentos

Crie uma classe base chamada Pagamento.

Essa classe deve possuir o método:
pagar(valor)

Depois crie quatro classes filhas:

- Pix
- CartaoCredito
- Boleto
- Criptomoeda

Cada classe deve implementar o método pagar()
mostrando como o pagamento está sendo realizado.

Exemplo:

Pagamento PIX de 100 realizado
Pagamento no cartão de 100 realizado
Boleto de 100 gerado
Pagamento em criptomoeda de 100 realizado

Crie uma função chamada finalizar_compra(pagamento, valor)
que recebe um objeto de pagamento e executa o método pagar().

A função não pode usar if para verificar o tipo de pagamento.
O comportamento deve ser resolvido usando polimorfismo.
"""
import qrcode

class Pagamento:
    def pagar(self, valor):
        raise NotImplementedError
    
class Pix(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento PIX de {valor} realizado")
        
        dados_pix = f"Pagamento PIX no valor de {valor}"
        qr = qrcode.make(dados_pix)
        qr.save("pix_qrcode.png")
        print("QR Code gerado: pix_qrcode.png")

class CartaoCredito(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento no cartão de {valor} realizado")

class Boleto(Pagamento):
    def pagar(self, valor):
        print(f"Boleto de {valor} gerado")

class Criptomoeda(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento em criptomoeda de {valor} realizado")

def finalizar_compra(pagamento, valor):
    pagamento.pagar(valor)

def menu_pagamento():
    print("\n=== SISTEMA DE PAGAMENTOS ===")
    print("Escolha a forma de pagamento:")
    print("1 - PIX")
    print("2 - Cartão de Crédito")
    print("3 - Boleto")
    print("4 - Criptomoeda")
    
    while True:
        try:
            opcao = int(input("Digite a opção (1-4): "))
            if 1 <= opcao <= 4:
                break
            else:
                print("Opção inválida! Digite um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    while True:
        try:
            valor = float(input("Digite o valor da compra: R$ "))
            if valor > 0:
                break
            else:
                print("Valor deve ser maior que zero!")
        except ValueError:
            print("Valor inválido! Digite um número.")
    
    if opcao == 1:
        pagamento = Pix()
    elif opcao == 2:
        pagamento = CartaoCredito()
    elif opcao == 3:
        pagamento = Boleto()
    elif opcao == 4:
        pagamento = Criptomoeda()
    
    print(f"\nProcessando pagamento de R$ {valor:.2f}...")
    finalizar_compra(pagamento, valor)
    print("Compra finalizada com sucesso!")

if __name__ == "__main__":
    menu_pagamento()

