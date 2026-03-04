class Aluno:
    def __init__ (self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def verifica_media(self):
        media = self.calcular_media()
    
        if media >= 7:
            return "APROVADO"
        
        elif media >= 5:
            return "RECUPERAÇÃO"
        
        else:
            return "REPROVADO"
    

    def exibir_dados(self):
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Média: {self.calcular_media():.2f}")
        print(f"Situação: {self.verifica_media()}")
        print("-" * 20)


alunos = []

while True:
    print("\n=== CADASTRAR ALUNO ===")
    quantidade = int(input("Quantos criterios de notas exixtem nesta sala: "))
    nome = input("Nome do aluno (ou 'sair'): ")

    if nome.lower() == "sair":
        break

    idade = int(input("Digite a idade do aluno: "))

    notas = []
    for i in range(quantidade):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota deve estar entre 0 e 10.")
            except ValueError:
                print("Digite um número válido.")

    aluno = Aluno(nome, idade, notas)
    alunos.append(aluno)

print("\n=== ALUNOS CADASTRADOS ===")
for aluno in alunos:
    aluno.exibir_dados()

