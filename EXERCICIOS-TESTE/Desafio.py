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