from twilio_files import *
from twilio.rest import Client

account_sid = account_sid
auth_token = auth_token
meu_numero = meu_numero #Recebe ligacao/sms
numero_twilio = numero_twilio #Faz ligacao/sms

client = Client(account_sid, auth_token)

escolha = int(input(f"Número: {meu_numero}\n1 - Ligar\n2 - Mensagem"))

if(escolha == 1):
    mensagem = """
        <Response>
            <Say language="pt-BR">
                Palmeiras não tem mundial
            </Say>
        </Response>
    """

    ligacao = client.calls.create(to=meu_numero, from_=numero_twilio, twiml=mensagem)

if(escolha == 2):
    mensagem = client.messages.create(to=meu_numero, from_=numero_twilio, body="Olá")
