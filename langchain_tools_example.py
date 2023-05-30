import os
from dotenv import load_dotenv

load_dotenv()

bruinen_client_id = os.getenv('BRUINEN_CLIENT_ID')
bruinen_secret = os.getenv('BRUINEN_SECRET')

from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from bruinen.src.bruinen.langchain.github import GithubGetProfileTool, GithubGetReposTool
from bruinen.src.bruinen.client import AuthenticatedClient

client = AuthenticatedClient(base_url='http://localhost:3000', token=bruinen_secret, prefix='', auth_header_name='X-API-Key')

# Update to the user ID you want to test with
user_id = '0a40131b-7c8a-4d0b-a2ba-a99e20db31ae'

llm = OpenAI(temperature=0)
# github = GithubGetReposTool(llm=llm, client=client, user_id=user_id)
github_profile = GithubGetProfileTool(client=client, user_id=user_id)
github_repos = GithubGetReposTool(client=client, user_id=user_id)
agent = initialize_agent([github_profile, github_repos], llm, agent='chat-zero-shot-react-description', verbose=True)
result = agent.run("What are my Github repos?")
