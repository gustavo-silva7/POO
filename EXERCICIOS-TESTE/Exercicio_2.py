"""
EXERCÍCIO 2 — Sistema de Notificações

Crie uma classe base chamada Notificacao.

Essa classe deve possuir o método:
enviar(mensagem)

Depois crie três classes filhas:

- Email
- SMS
- PushNotification

Cada classe deve sobrescrever o método enviar() e exibir
a mensagem de forma diferente.

Exemplo esperado:

Enviando EMAIL: Olá usuário
Enviando SMS: Olá usuário
Enviando PUSH: Olá usuário

Depois crie uma função que receba um objeto de notificação
e uma mensagem e execute o envio.

A função não pode saber qual tipo de notificação está sendo usada.
"""

class Notifica:
    def enviar_msg(self):
        raise NotImplementedError
    
class Email(Notifica):
    def enviar_msg(self):
        print("Envando Email: Olá mundo")

class SMS(Notifica):
    def enviar_msg(self):
        print("Envando SMS: Olá mundo")

class PushNotification(Notifica):
    def enviar_msg(self):
        print("Envando PUSH: Olá mundo")

notificacao = [Email(), SMS(), PushNotification()]

for n in notificacao:
    n.enviar_msg()