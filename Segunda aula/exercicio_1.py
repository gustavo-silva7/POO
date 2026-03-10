'''
EXERCÍCIO 1 – Classe Pessoa
Crie uma classe chamada Pessoa com:
Atributos:
● nome
● idade
Método:
● apresentar() → deve exibir:
Olá, meu nome é (nome) e tenho (idade) anos.
Agora crie duas classes filhas:
● Aluno
● Professor
Regras
A classe Aluno deve possuir:
● atributo: curso
● método: estudar()
Mensagem:
(nome) está estudando (curso)
A classe Professor deve possuir:
● atributo: disciplina
● método: ensinar()
Mensagem:
(nome) está ensinando (disciplina
'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos!")


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def estudar(self):
        print(f"Aluno(a) {self.nome} está estudando {self.curso}!")


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def ensinar(self):
        print(f"Professor(a) {self.nome} está ensinando {self.disciplina}")


# aluno = Aluno("Carlos", 20, "Python")
# professor = Professor("Ana", 40, "Programação")

# aluno.apresentar()
# aluno.estudar()

# professor.apresentar()
# professor.ensinar()


pessoas = [ ]
while True:
    tipo = input("Digite (A) para alunos ou (P) para professor ou (S) para sair: ").strip().lower()

    if tipo in ['a', 'p']:
        nome = input("Nome: ")
        idade = int(input("Idade: "))

    elif tipo == 's':
        break

    else:
        print("RESPOSTA INVALIDA!")
        continue

    if tipo == 'a':
        curso = input("Curso: ")
        pessoas.append(Aluno(nome,idade,curso))
    
    if tipo == 'p':
        disciplina = input("Nome da disciplina: ")
        pessoas.append(Professor(nome, idade, disciplina))

for pessoa in pessoas:

    pessoa.apresentar()

    if isinstance(pessoa, Aluno):
        pessoa.estudar()

    elif isinstance(pessoa, Professor):
        pessoa.ensinar()
