from twilio_files import *
from twilio.rest import Client

account_sid = account_sid
auth_token = auth_token
meu_numero = meu_numero #Recebe ligacao/sms
numero_twilio = numero_twilio #Faz ligacao/sms

client = Client(account_sid, auth_token)

# mensagem = """
#     <Response>
#         <Say language="pt-BR">
#             Testando mensagem programada
#         </Say>
#     </Response>
# """

#ligacao = client.calls.create(to=meu_numero, from_=numero_twilio, twiml=mensagem)
mensage = client.messages.create(to=meu_numero, from_=numero_twilio, body="Olá")
