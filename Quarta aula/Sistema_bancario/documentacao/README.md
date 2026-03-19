# Documentação do Sistema Bancário

## Visão geral
Este projeto é um sistema bancário em Python com CLI e banco SQLite. A arquitetura é separada por responsabilidades:

- `main.py`: interface de terminal (menu, entradas e fluxo de usuário)
- `banco.py`: operações de banco de dados (SQLite)
- `models.py`: modelos de domínio (`Cliente`, `Conta`)
- `services.py`: regras de negócio (cadastro, login, depósito, saque, saldo)

## Tecnologias
- Python 3
- SQLite3
- Hash de senha: `hashlib`

## Estrutura de diretórios
```
Sistema_bancario/
  ├─ banco.py
  ├─ main.py
  ├─ models.py
  ├─ services.py
  └─ documentacao/
      └─ README.md
```

## Banco de dados
O banco `banco.db` é criado automaticamente na primeira execução. A tabela `contas` contém:

- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `nome` TEXT NOT NULL
- `cpf` TEXT UNIQUE NOT NULL
- `data_nascimento` TEXT NOT NULL
- `senha` TEXT NOT NULL (hash SHA-256)
- `saldo` REAL DEFAULT 0

## Funcionalidades
1. Criar conta (nome, cpf, data de nascimento, senha)
2. Login (CPF + senha)
3. Depositar (valor positivo)
4. Sacar (validar saldo suficiente)
5. Ver saldo
6. Logout

## Como executar
1. Abra terminal no diretório `Quarta aula/Sistema_bancario`
2. Execute:

```bash
python3 main.py
```
3. Use o menu para interagir.

## Regras de negócio implementadas
- CPF único (gerencia `sqlite3.IntegrityError` e retorna mensagem amigável)
- Senha armazenada como hash SHA-256 (`hashlib`)
- Conexões feitas com `with sqlite3.connect(...)`
- Queries parametrizadas (`?`)
- Não é permitido saque com saldo insuficiente
- Depósitos e saques exigem valor maior que zero

## Possíveis melhorias futuras
- Extrair validação de CPF para funções utilitárias
- Adicionar histórico de transações e extrato
- Permitir alteração de senha
- Adicionar camada de testes unitários

---

Se quiser, posso criar um `docs/arquitetura.md` e um `docs/fluxo.md` com diagramas simples para documentação interna.