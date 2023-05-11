import os, requests, base64, pytz

# TODO try removing
os.environ['OPENAI_API_KEY'] = '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'
os.environ['BRUINEN_SECRET'] = 'clg79qu20000muk22tlx0tybn'

from datetime import datetime
from langchain import SQLDatabase, SQLDatabaseChain
from langchain.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate
from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from connect import generateConnectUrl

class BruinenVenmo:
    name = 'Venmo transaction history'
    description = 'Useful for when you need to pull purchases made with Venmo. Pass the tool the question that you want to know and it will give you the answer.'
        
    def __init__(self):
        self.user_id = ''

    def run(self, query):
        secret = os.environ['BRUINEN_SECRET']
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': secret
        }

        res_accounts = requests.get(f'https://api.bruinen.co/accounts/user/{self.user_id}', headers=headers)
        connected_accounts = res_accounts.json()

        account_id = ''
        for account in connected_accounts:
            if account['source'] == 'venmo':
                account_id = account['id']
        if account_id == '':
            # User has not authenticated Venmo, return the Connect string
            return 'The user has not connected their Venmo account; you should try authenticating Venmo'
        else:
            res_transactions = requests.get(f'https://api.bruinen.co/sources/venmo/transactions?accountId={account_id}', headers=headers)
            transactions = res_transactions.json()
            
            # Create a SQLite database with a purchase table to use for the SQL chain
            engine = create_engine('sqlite:///notebooks/venmo.db', echo=True)
            Base = declarative_base()

            class Purchase(Base):
                __tablename__ = 'purchase'
                
                id = Column(Integer, primary_key=True)
                date_time = Column(DateTime)
                peer = Column(String)
                transaction_type = Column(String)
                amount_in_cents = Column(Integer)
                memo = Column(String)

            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            # Loop through the JSON transactions and add them to the created table
            data = []
            for transaction in transactions['transactions']:
                if transaction['transaction_type'] != 'payment':
                    continue
                
                date = transaction['datetime_created']
                dt_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
                
                peer = transaction['peer']['display_name']
                transaction_type = transaction['movement_type']
                amount_in_cents = transaction['amount_in_cents']
                memo = transaction['memo'].replace('\n', '')

                data.append({
                    'date_time': dt_obj,
                    'peer': peer,
                    'transaction_type': transaction_type,
                    'amount_in_cents': amount_in_cents,
                    'memo': memo
                })
            session.bulk_insert_mappings(Purchase, data)
            session.commit()
            session.close()

            # Run a SQLDatabaseChain on the created table with the provided query 
            _DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
            Use the following format:

            Question: "Question here"
            SQLQuery: "SQL Query to run"
            SQLResult: "Result of the SQLQuery"
            Answer: "Final answer here"

            Only use the following tables:

            {table_info}

            Question: {input}"""
            PROMPT = PromptTemplate(input_variables=['input', 'table_info', 'dialect'], template=_DEFAULT_TEMPLATE)
            db = SQLDatabase.from_uri('sqlite:///notebooks/venmo.db')
            llm = OpenAI(temperature=0)
            db_chain = SQLDatabaseChain(llm=llm, database=db, prompt=PROMPT, verbose=True)
            res = db_chain.run(query)

            # Drop the created table so it doesn't overwrite later
            metadata = MetaData()
            metadata.reflect(bind=engine)
            mytable = Table('purchase', metadata, autoload=True, autoload_with=engine)
            mytable.drop(engine)

            return res

# BruinenVenmoAuthenticator
# TODO add description
class BruinenVenmoAuthenticator:
    name = 'Venmo authenticator'
    description = 'Useful for when a user\'s Venmo account is not authenticated. The response from the tool will be a URL that you return to the user for them to compete auth. This URL will be your final answer.'

    def __init__(self):
        self.user_token = ''

    def run(self, query):
        url = generateConnectUrl(self.user_token, 'venmo')
        return url

# BruinenGmail
# TODO add description  
class BruinenGmail:
    name = 'Gmail message history'
    description = 'Useful for when you need to pull emails in Gmail. Pass the tool the question that you want to know and it will give you the answer.'
        
    def __init__(self):
        self.user_id = ''

    def run(self, query):
        secret = os.environ['BRUINEN_SECRET']
        headers = {
            'Content-Type': 'application/json',
            'X-API-Key': secret
        }

        res_accounts = requests.get(f'https://api.bruinen.co/accounts/user/{self.user_id}', headers=headers)
        connected_accounts = res_accounts.json()

        account_id = ''
        for account in connected_accounts:
            if account['source'] == 'google':
                account_id = account['id']
        if account_id == '':
            # User has not authenticated Gmail, return the connect string
            return 'The user has not connected their Gmail account; you should try authenticating Gmail'
        else:
            res_messages = requests.get(f'https://api.bruinen.co/sources/google/gmailMessages?accountId={account_id}', headers=headers)
            messages = res_messages.json()
            counter = 0
            for message in messages['messages']:
                counter += 1
                # Only use the 50 most recent emails
                if counter > 50:
                    break
                message_id = message['id']
                res_message = requests.get(f'https://api.bruinen.co/sources/google/gmailMessage?accountId={account_id}&messageId={message_id}', headers=headers)
                payload = res_message.json()['payload']

                message_data = {}

                # Pull name of sender, email of sender, date of email from headers
                message_headers = payload['headers']
                for header in message_headers:
                    if header['name'] == 'Date':
                        date_string = header['value']
                        # Truncate any date strings with (UTC), (CDT), or similar at the end
                        if header['value'][-1] == ')':
                            date_string = header['value'][:-6]
                        date_object = datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z')
                        utc_timezone = pytz.timezone('UTC')
                        utc_date = date_object.astimezone(utc_timezone)
                        message_data['date_time'] = utc_date
                    if header['name'] == 'From':
                        names = header['value'].split('<')
                        message_data['name'] = names[0].strip()
                        message_data['email'] = names[1][:-1]

                # Parts can have sub-parts so we need to pull the message text recursively
                def text_recursive(parts):
                    text = ''
                    for part in parts:
                        if 'body' in part:
                            if 'data' in part['body']:
                                # Don't collect HTML parts, only plain text
                                if part['mimeType'] == 'text/plain':
                                    data = part['body']['data']
                                    decoded_bytes = base64.urlsafe_b64decode(data + "=" * ((4 - len(data) % 4) % 4))
                                    decoded_string = decoded_bytes.decode("utf-8")
                                    text += decoded_string
                        if 'parts' in part:
                            text += text_recursive(part['parts'])
                    return text
                                
                message_data['body'] = text_recursive(payload['parts'])


            
            # print(messages)
            return ''
            # Create a SQLite database with a purchase table to use for the SQL chain
            engine = create_engine('sqlite:///notebooks/venmo.db', echo=True)
            Base = declarative_base()

            class Purchase(Base):
                __tablename__ = 'purchase'
                
                id = Column(Integer, primary_key=True)
                date_time = Column(DateTime)
                peer = Column(String)
                transaction_type = Column(String)
                amount_in_cents = Column(Integer)
                memo = Column(String)

            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            # Loop through the JSON transactions and add them to the created table
            data = []
            for transaction in transactions['transactions']:
                if transaction['transaction_type'] != 'payment':
                    continue
                
                date = transaction['datetime_created']
                dt_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
                
                peer = transaction['peer']['display_name']
                transaction_type = transaction['movement_type']
                amount_in_cents = transaction['amount_in_cents']
                memo = transaction['memo'].replace('\n', '')

                data.append({
                    'date_time': dt_obj,
                    'peer': peer,
                    'transaction_type': transaction_type,
                    'amount_in_cents': amount_in_cents,
                    'memo': memo
                })
            session.bulk_insert_mappings(Purchase, data)
            session.commit()
            session.close()

            # Run a SQLDatabaseChain on the created table with the provided query 
            _DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
            Use the following format:

            Question: "Question here"
            SQLQuery: "SQL Query to run"
            SQLResult: "Result of the SQLQuery"
            Answer: "Final answer here"

            Only use the following tables:

            {table_info}

            Question: {input}"""
            PROMPT = PromptTemplate(input_variables=['input', 'table_info', 'dialect'], template=_DEFAULT_TEMPLATE)
            db = SQLDatabase.from_uri('sqlite:///notebooks/venmo.db')
            llm = OpenAI(temperature=0)
            db_chain = SQLDatabaseChain(llm=llm, database=db, prompt=PROMPT, verbose=True)
            res = db_chain.run(query)

            # Drop the created table so it doesn't overwrite later
            metadata = MetaData()
            metadata.reflect(bind=engine)
            mytable = Table('purchase', metadata, autoload=True, autoload_with=engine)
            mytable.drop(engine)

            return res
        
# BruinenGmailAuthenticator
# TODO add description
class BruinenGmailAuthenticator:
    name = 'Gmail authenticator'
    description = 'Useful for when a user\'s Gmail account is not authenticated. The response from the tool will be a URL that you return to the user for them to compete auth. This URL will be your final answer.'

    def __init__(self):
        self.user_token = ''

    def run(self, query):
        url = generateConnectUrl(self.user_token, 'google')
        return url