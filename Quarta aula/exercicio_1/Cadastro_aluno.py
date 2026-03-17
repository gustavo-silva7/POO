# Sistema de Cadastro de Alunos
# O sistema deve permitir:
# Cadastrar alunos
# Listar alunos cadastrados
# Buscar aluno pelo nome
# Mostrar informações do aluno
# Estrutura sugerida
# Classe Aluno
# Atributos:
# nome
# idade
# curso
# matrícula
# Métodos:
# mostrar_dados()
# Sistema de Cadastro de Alunos com Polimorfismo

from datetime import datetime, date
import os

class Aluno:
    contador = 1

    def __init__(self, nome, data_nascimento, curso, matricula=None):

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.curso = curso

        if matricula:
            self.matricula = int(matricula)
        else:
            ano = date.today().year
            self.matricula = int(f"{ano}{Aluno.contador:04d}")
            Aluno.contador += 1

    def calcula_idade(self):

        nascimento = datetime.strptime(self.data_nascimento, "%d/%m/%Y").date()
        hoje = date.today()

        idade = hoje.year - nascimento.year - (
            (hoje.month, hoje.day) < (nascimento.month, nascimento.day)
        )

        return idade

    def calcular_mensalidade(self):
        raise NotImplementedError

    def mostrar_dados(self):

        print("\n===== DADOS DO ALUNO =====")
        print(f"Nome: {self.nome}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"Idade: {self.calcula_idade()} anos")
        print(f"Curso: {self.curso}")
        print(f"Matrícula: {self.matricula}")
        print(f"Mensalidade: R${self.calcular_mensalidade()}")
        print("==========================\n")

class AlunoGraduacao(Aluno):

    def calcular_mensalidade(self):
        return 800


class AlunoPos(Aluno):

    def calcular_mensalidade(self):
        return 1200


class AlunoTecnico(Aluno):

    def calcular_mensalidade(self):
        return 500


alunos = []

def salvar_aluno(aluno):

    with open("alunos.txt", "a", encoding="utf-8") as arquivo:

        tipo = aluno.__class__.__name__

        arquivo.write(
            f"{tipo};{aluno.nome};{aluno.data_nascimento};{aluno.curso};{aluno.matricula}\n"
        )


def carregar_alunos():

    if not os.path.exists("alunos.txt"):
        return

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:

        for linha in arquivo:

            tipo, nome, data, curso, matricula = linha.strip().split(";")

            if tipo == "AlunoGraduacao":
                aluno = AlunoGraduacao(nome, data, curso, matricula)

            elif tipo == "AlunoPos":
                aluno = AlunoPos(nome, data, curso, matricula)

            elif tipo == "AlunoTecnico":
                aluno = AlunoTecnico(nome, data, curso, matricula)

            alunos.append(aluno)

def cadastrar_aluno():

    nome = input("Nome: ")
    data = input("Data de nascimento (dd/mm/aaaa): ")
    curso = input("Curso: ")

    print("\nTipo de aluno")
    print("1 - Graduação")
    print("2 - Pós-graduação")
    print("3 - Técnico")

    tipo = input("Escolha: ")

    if tipo == "1":
        aluno = AlunoGraduacao(nome, data, curso)

    elif tipo == "2":
        aluno = AlunoPos(nome, data, curso)

    elif tipo == "3":
        aluno = AlunoTecnico(nome, data, curso)

    else:
        print("Tipo inválido")
        return

    alunos.append(aluno)

    salvar_aluno(aluno)

    print("Aluno cadastrado com sucesso!\n")


def listar_alunos():

    if not alunos:
        print("Nenhum aluno cadastrado\n")
        return

    print("\n===== LISTA DE ALUNOS =====")

    for aluno in alunos:
        aluno.mostrar_dados()


def buscar_aluno():

    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:

        if aluno.nome.lower() == nome.lower():
            aluno.mostrar_dados()
            return

    print("Aluno não encontrado\n")


carregar_alunos()

while True:

    print("===== SISTEMA DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        buscar_aluno()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida\n")