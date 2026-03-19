from dataclasses import dataclass


@dataclass
class Cliente:
    id: int
    nome: str
    cpf: str
    data_nascimento: str
    senha_hash: str
    saldo: float


@dataclass
class Conta:
    cliente: Cliente

    def __post_init__(self):
        # Em um sistema maior, aqui podemos adicionar lógica para validação adicional
        pass
