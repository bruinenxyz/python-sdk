import os
from dotenv import load_dotenv

load_dotenv()

bruinen_client_id = os.getenv('BRUINEN_CLIENT_ID')
bruinen_secret = os.getenv('BRUINEN_SECRET')

from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from bruinen.src.bruinen.langchain.github import GithubGetProfileTool, GithubGetReposTool
from bruinen.src.bruinen.langchain.google import GoogleGetDraftsTool, GoogleAuthenticatorTool
from bruinen.src.bruinen.client import AuthenticatedClient

client = AuthenticatedClient(base_url='http://localhost:3000', token=bruinen_secret, prefix='', auth_header_name='X-API-Key')

# Google parsed drafts example

llm = OpenAI(temperature=0)

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from bruinen.src.bruinen.langchain.google import GoogleGetParsedMessagesTool

def parse_parameters(_query: str) -> GoogleGetParsedMessagesTool.input_schema:
    # Parse the q parameter
    _prompt = PromptTemplate(
        input_variables=["query"],
        template="""
        Given the provided input query, output a response that adheres to the following syntax:

        To the specify the sender:
        from:sender
        Example: from:amy

        To specify a recipient: 
        to:recipient
        Example: to:david

        To specify a recipient who received a cc:
        cc:recipient
        Example: cc:david

        To specify a recipient who received a bcc:
        bcc:recipient
        Example: bcc:david

        To specify words in the subject line:
        subject:words
        Example: subject:dinner

        To specify messages that match multiple terms:
        term1 OR term2
        Example: from:amy OR from:david

        To search for an exact word or phrase in the message or subject line:
        "word or phrase"
        Example: "dinner and movie tonight"
        
        If anything in the input query does not relate to functionality in the above description, do not include it in the response.
        Exclude anything related to page tokens and labels.
        If no response is necessary for the input query, respond with an empty string.

        Here is the input query:

        {query}
        """
    )
    q_parser_chain = LLMChain(llm=llm, prompt=_prompt)
    parsed_q = q_parser_chain.run(query=_query)

    # For now, we'll ignore the labelId and pageToken parameters
    params = GoogleGetParsedMessagesTool.input_schema()
    print(parsed_q)
    params.q = parsed_q.strip()

    return params

user_id = '0a40131b-7c8a-4d0b-a2ba-a99e20db31ae'
llm = OpenAI(temperature=0)

from bruinen.src.bruinen.client.models import GoogleParsedMessages, GoogleParsedMessage, GoogleParsedMessagesMessagesItem
from bruinen.src.bruinen.langchain.parsers import SQLParser
from typing import List, Dict, Any
from pydantic import Field
from datetime import datetime

def parse_output(output: GoogleParsedMessages, query: str):
    messages: List["GoogleParsedMessagesMessagesItem"] = output.messages

    # Get a usable table from the messages
    class MessagesItem:
        from_name: str = Field(description="The name of the sender")
        from_email: str = Field(description="The email of the sender")
        date_time: datetime = Field(description="The date and time the message was sent")
        to_emails: List[str] = Field(description="The emails of the recipients")
        cc_emails: List[str] = Field(description="The emails of the recipients who received a cc")
        bcc_emails: List[str] = Field(description="The emails of the recipients who received a bcc")
        subject: str = Field(description="The subject of the message")
        body: str = Field(description="The body of the message")
        
        def __init__(self, from_name, from_email, date_time, subject, body, to_emails, cc_emails, bcc_emails):
            self.from_name = from_name
            self.from_email = from_email
            self.date_time = date_time
            self.subject = subject
            self.body = body
            self.to_emails = to_emails
            self.cc_emails = cc_emails
            self.bcc_emails = bcc_emails

        def to_dict(self) -> Dict[str, Any]:
            fields = {}
            fields['from_name'] = self.from_name
            fields['from_email'] = self.from_email
            fields['date_time'] = self.date_time
            fields['subject'] = self.subject
            fields['body'] = self.body
            fields['to_emails'] = self.to_emails
            fields['cc_emails'] = self.cc_emails
            fields['bcc_emails'] = self.bcc_emails
            return fields

    parsed_messages: List["MessagesItem"] = []

    for m in messages:
        message = m.to_dict()
        if 'name' in message['headers']['from'].keys():
            from_name = message['headers']['from']['name']
        else:
            from_name = ''
        from_email = message['headers']['from']['email']
        date_time_str = message['headers']['date']
        if "(" in date_time_str:
            date_time_str = date_time_str[:date_time_str.index("(")].strip()
        date_format = "%a, %d %b %Y %H:%M:%S %z"
        date_time = datetime.strptime(date_time_str, date_format)
        if 'subject' in message['headers'].keys():
            subject = message['headers']['subject']
        else:
            subject = ''
        if 'body' in message.keys():
            body = message['body']
        else:
            body = ''
        to_emails = []
        for recipient in message['headers']['to']:
            to_emails.append(recipient['email'])
        cc_emails = []
        for cc in message['headers']['cc']:
            cc_emails.append(cc['email'])
        bcc_emails = []
        for bcc in message['headers']['bcc']:
            bcc_emails.append(bcc['email'])

        parsed_message = MessagesItem(
            from_name = from_name,
            from_email = from_email,
            date_time = date_time,
            subject = subject,
            body = body,
            to_emails = to_emails,
            cc_emails = cc_emails,
            bcc_emails = bcc_emails
        )

        parsed_messages.append(parsed_message)

    llm = OpenAI(temperature=0)
    parser = SQLParser(llm=llm)
    result = parser.parse(parsed_messages, query)

    return result

tool = GoogleGetParsedMessagesTool(client=client, user_id=user_id, parse_output=parse_output, parse_parameters=parse_parameters, llm=llm)
agent = initialize_agent([tool], llm, agent='chat-zero-shot-react-description', verbose=True)
result = agent.run("What is the body of the most recent message that is either to or from tevon@bruinen.co?")

exit()

## Google example

user_id = '0a40131b-7c8a-4d0b-a2ba-a99e20db31ae'

input_llm = OpenAI(temperature=0)
agent_llm = OpenAI(temperature=0)
def parse_drafts(output, query):
    print(query)
    print(output)
    return output
google_drafts_tool = GoogleGetDraftsTool(client=client, user_id=user_id, llm=input_llm, parse_output=parse_drafts)
agent = initialize_agent([google_drafts_tool], agent_llm, agent='chat-zero-shot-react-description', verbose=True)
result = agent.run("What are my Google drafts with q=null and pageToken='1'?")

## Github example

# Update to the user ID you want to test with
user_id = '0a40131b-7c8a-4d0b-a2ba-a99e20db31ae'

 # Create a tool to pull your Github repos with a SQL output parser
from bruinen.src.bruinen.langchain.parsers import SQLParser
repos_llm = OpenAI(temperature=0)
sql_parser = SQLParser(llm = repos_llm)
github_repos_tool = GithubGetReposTool(client=client, user_id=user_id, parse_output=sql_parser.parse)

# Create a tool to pull your Github profile with a custom output parser
profile_llm = OpenAI(temperature=0)
def parse_profile(output, query):
    print(output, query)
    return 'Example response from custom tool.'
github_profile_tool = GithubGetProfileTool(client=client, user_id=user_id, parse_output=parse_profile)

# Run an agent with both tools added
agent_llm = OpenAI(temperature=0)
agent = initialize_agent([github_repos_tool, github_profile_tool], agent_llm, agent='chat-zero-shot-react-description', verbose=True)
result = agent.run("What does my Github profile look like?")
