import sqlite3

DB_PATH = "banco.db"


def init_db():
    """Inicializa o banco e cria a tabela se não existir."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                data_nascimento TEXT NOT NULL,
                senha TEXT NOT NULL,
                saldo REAL DEFAULT 0
            );
            """
        )
        conn.commit()


def create_account(nome: str, cpf: str, data_nascimento: str, senha_hash: str):
    """Insere nova conta no banco. Lança sqlite3.IntegrityError se CPF duplicado."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contas (nome, cpf, data_nascimento, senha, saldo) VALUES (?, ?, ?, ?, 0)",
            (nome, cpf, data_nascimento, senha_hash),
        )
        conn.commit()
        return cursor.lastrowid


def get_account_by_cpf(cpf: str):
    """Retorna o registro da conta pelo CPF ou None."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, cpf, data_nascimento, senha, saldo FROM contas WHERE cpf = ?", (cpf,))
        return cursor.fetchone()


def update_balance(conta_id: int, novo_saldo: float):
    """Atualiza saldo para a conta especificada."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE contas SET saldo = ? WHERE id = ?", (novo_saldo, conta_id))
        conn.commit()


def get_balance(conta_id: int):
    """Retorna o saldo atual da conta."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT saldo FROM contas WHERE id = ?", (conta_id,))
        row = cursor.fetchone()
        return row[0] if row else None
