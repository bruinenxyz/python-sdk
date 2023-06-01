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

# Things to do:
#   Handle input (query, parameters, etc.)
