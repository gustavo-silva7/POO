import hashlib
from banco import get_account_by_cpf, create_account, update_balance, get_balance
from models import Cliente


def hash_password(senha: str) -> str:
    """Retorna hash SHA-256 da senha."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def criar_conta(nome: str, cpf: str, data_nascimento: str, senha: str) -> Cliente:
    """Cria conta verificando CPF único e retornando cliente."""
    existente = get_account_by_cpf(cpf)
    if existente:
        raise ValueError("CPF já cadastrado.")

    senha_hash = hash_password(senha)
    conta_id = create_account(nome, cpf, data_nascimento, senha_hash)
    return Cliente(id=conta_id, nome=nome, cpf=cpf, data_nascimento=data_nascimento, senha_hash=senha_hash, saldo=0.0)


def login(cpf: str, senha: str) -> Cliente:
    """Valida CPF e senha e retorna Cliente se correto."""
    row = get_account_by_cpf(cpf)
    if not row:
        raise ValueError("CPF não encontrado.")

    conta_id, nome, cpf_db, data_nascimento, senha_hash_db, saldo = row
    if hash_password(senha) != senha_hash_db:
        raise ValueError("Senha incorreta.")

    return Cliente(id=conta_id, nome=nome, cpf=cpf_db, data_nascimento=data_nascimento, senha_hash=senha_hash_db, saldo=saldo)


def fazer_deposito(cliente: Cliente, valor: float) -> float:
    """Depósito: aceita valor positivo e retorna novo saldo."""
    if valor <= 0:
        raise ValueError("Valor de depósito deve ser maior que zero.")

    saldo_atual = get_balance(cliente.id)
    if saldo_atual is None:
        raise ValueError("Conta não encontrada.")

    novo_saldo = saldo_atual + valor
    update_balance(cliente.id, novo_saldo)
    cliente.saldo = novo_saldo
    return novo_saldo


def fazer_saque(cliente: Cliente, valor: float) -> float:
    """Saque: valor positivo e saldo suficiente."""
    if valor <= 0:
        raise ValueError("Valor de saque deve ser maior que zero.")

    saldo_atual = get_balance(cliente.id)
    if saldo_atual is None:
        raise ValueError("Conta não encontrada.")

    if valor > saldo_atual:
        raise ValueError("Saldo insuficiente.")

    novo_saldo = saldo_atual - valor
    update_balance(cliente.id, novo_saldo)
    cliente.saldo = novo_saldo
    return novo_saldo


def obter_saldo(cliente: Cliente) -> float:
    """Retorna o saldo atual da conta."""
    saldo = get_balance(cliente.id)
    if saldo is None:
        raise ValueError("Conta não encontrada.")
    cliente.saldo = saldo
    return saldo
