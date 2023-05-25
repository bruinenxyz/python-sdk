import os
from dotenv import load_dotenv

load_dotenv()

bruinen_client_id = os.getenv('BRUINEN_CLIENT_ID')
bruinen_secret = os.getenv('BRUINEN_SECRET')

from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from bruinen_sdk.langchain_tools.github_test import GithubGetReposTool
from bruinen_sdk.bruinen_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url='http://localhost:3000', token=bruinen_secret, prefix='', auth_header_name='X-API-Key')

# Update to the user ID you want to test with
user_id = '0a40131b-7c8a-4d0b-a2ba-a99e20db31ae'

llm = OpenAI(temperature=0)
github = GithubGetReposTool(llm=llm, client=client, user_id=user_id)
agent = initialize_agent([github], llm, agent='chat-zero-shot-react-description', verbose=True)
result = agent.run("What are my Github repos?")
