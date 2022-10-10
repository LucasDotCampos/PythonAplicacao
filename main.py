import pandas as pd 
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


account_sid = os.environ['twilio_id']
auth_token  = os.environ['twilio_token']
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'maio', 'junho']

for mes in lista_meses:
     tabela_vendas = pd.read_excel(f'./database/{mes}.xlsx')
     if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to=os.environ['my_phone_number'],
            from_=os.environ['twilio_phone_number'],
            body=f'No mês {mes}  o vendedor {vendedor} conseguiu vender R${vendas}')
        print(message.sid)

