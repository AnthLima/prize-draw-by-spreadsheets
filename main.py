import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfcd43b45681dc4434c736a600f57652e"
# Your Auth Token from twilio.com/console
auth_token  = "780c136a6b2d713917e5b73340e2db82"

listOfMonths = ['janeiro','fevereiro','março','abril','maio','junho']


for month in listOfMonths:
    salesTable = pd.read_excel(f'./excel_files/{month}.xlsx')
    if (salesTable['Vendas'] > 55000).any():
        seller = salesTable.loc[salesTable['Vendas'] >= 55000 , 'Vendedor']
        sales = salesTable.loc[salesTable['Vendas'] >= 55000 , 'Vendas']
        print(f'No mes {month} alguém bateu a meta. Vendedor: {seller}, Vendas: {sales}')





client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5584986460017", 
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)