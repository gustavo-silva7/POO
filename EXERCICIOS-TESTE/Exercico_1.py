"""
EXERCÍCIO 1 — Sistema de Funcionários

Crie uma classe base chamada Funcionario.

Essa classe deve possuir o método:
calcular_pagamento()

Depois crie três classes que herdam de Funcionario:

- FuncionarioCLT
- Freelancer
- Estagiario

Cada classe deve sobrescrever o método calcular_pagamento()
e mostrar um valor diferente de pagamento.

Exemplo esperado de saída:

Funcionario CLT recebeu: 3000
Freelancer recebeu: 1500
Estagiario recebeu: 800

Depois crie uma lista contendo diferentes funcionários e percorra
essa lista chamando o método calcular_pagamento() para cada objeto.

Não utilize estruturas if para identificar o tipo do funcionário.
"""
class Funcionario:
    def calcula_pagamento(self):
        raise NotImplementedError

class FuncionarioCLT(Funcionario):
    def calcula_pagamento(self):
        print(f"Funcionario CLT recebeu: 3000")

class Freelancer(Funcionario):
    def calcula_pagamento(self):
        print(f"Freelancer recebeu: 1500")

class Estagiario(Funcionario):
    def calcula_pagamento(self):
        print(f"Freelancer recebeu: 800")

funcionarios = [FuncionarioCLT(), Freelancer(), Estagiario()]

for f in funcionarios:
    f.calcula_pagamento()