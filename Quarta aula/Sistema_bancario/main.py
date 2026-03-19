from banco import init_db
from services import criar_conta, login, fazer_deposito, fazer_saque, obter_saldo


def exibir_menu(logado: bool):
    print("\n--- Sistema Bancário ---")
    print("1 - Criar conta")
    print("2 - Login")
    if logado:
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Ver saldo")
        print("6 - Logout")
    print("0 - Sair")


def main():
    init_db()
    usuario_logado = None

    while True:
        exibir_menu(logado=usuario_logado is not None)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome: ").strip()
            cpf = input("CPF (somente números): ").strip()
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
            senha = input("Senha: ").strip()
            try:
                conta = criar_conta(nome, cpf, data_nascimento, senha)
                print(f"Conta criada com sucesso. ID: {conta.id}")
            except Exception as e:
                print(f"Erro ao criar conta: {e}")

        elif opcao == "2":
            if usuario_logado is not None:
                print("Já está logado. Faça logout antes de entrar com outra conta.")
                continue
            cpf = input("CPF: ").strip()
            senha = input("Senha: ").strip()
            try:
                usuario_logado = login(cpf, senha)
                print(f"Bem-vindo, {usuario_logado.nome}!")
            except Exception as e:
                print(f"Erro de login: {e}")

        elif opcao == "3" and usuario_logado is not None:
            try:
                valor = float(input("Valor para depositar: ").strip())
                novo_saldo = fazer_deposito(usuario_logado, valor)
                print(f"Depósito realizado. Saldo atual: R$ {novo_saldo:.2f}")
            except Exception as e:
                print(f"Erro no depósito: {e}")

        elif opcao == "4" and usuario_logado is not None:
            try:
                valor = float(input("Valor para sacar: ").strip())
                novo_saldo = fazer_saque(usuario_logado, valor)
                print(f"Saque realizado. Saldo atual: R$ {novo_saldo:.2f}")
            except Exception as e:
                print(f"Erro no saque: {e}")

        elif opcao == "5" and usuario_logado is not None:
            try:
                saldo = obter_saldo(usuario_logado)
                print(f"Saldo atual: R$ {saldo:.2f}")
            except Exception as e:
                print(f"Erro ao obter saldo: {e}")

        elif opcao == "6" and usuario_logado is not None:
            usuario_logado = None
            print("Logout realizado com sucesso.")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
