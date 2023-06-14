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

## Authenticator tool example


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

        If you want to the specify the sender:
        from:sender
        Example: from:amy

        If you want to specify a recipient: 
        to:recipient
        Example: to:david

        If you want to specify a recipient who received a cc:
        cc:recipient
        Example: cc:david

        If you want to specify a recipient who received a bcc:
        bcc:recipient
        Example: bcc:david

        If you want to specify words in the subject line:
        subject:words
        Example: subject:dinner

        If you want to specify messages that match multiple terms:
        term1 OR term2
        Example: from:amy OR from:david

        If you want to search for an exact word or phrase in the message or subject line:
        "word or phrase"
        Example: "dinner and movie tonight"
        
        If anything in the input query does not relate to functionality in the above description, do not include it in the response.
        For example, exlude anything related to page tokens and labels.

        Here is the input query:

        {query}
        """
    )
    q_parser_chain = LLMChain(llm=llm, prompt=_prompt)
    parsed_q = q_parser_chain.run(query=_query)
    print('parsed q parameter', parsed_q)

    # Parse all the other parameters except for q
    parser = PydanticOutputParser(pydantic_object=GoogleGetParsedMessagesTool.input_schema)
    prompt = PromptTemplate(
        template="""Parse the provided input string.
        For values that are not marked as required, if no value is provided, return a null value.
        {format_instructions}
        Here is the input:
        {query}""",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    _input = prompt.format_prompt(query=_query)
    pydantic_llm = OpenAI(temperature=0)
    output = pydantic_llm(_input.to_string())
    params: GoogleGetParsedMessagesTool.input_schema = parser.parse(output)
    print('params except q', params)
    params.q = parsed_q.strip()

    print('all params', params)

    return params



print(parse_parameters("What are my Google messages that are to or from tevon@bruinen.co, and contain with pageToken='1'?"))

user_id = '0a40131b-7c8a-4d0b-a2ba-a99e20db31ae'
llm = OpenAI(temperature=0)

def parse_output(output, query):
    print(output)
    return output

tool = GoogleGetParsedMessagesTool(client=client, user_id=user_id, parse_output=parse_output, parse_parameters=parse_parameters, llm=llm)
agent = initialize_agent([tool], llm, agent='chat-zero-shot-react-description', verbose=True)
result = agent.run("What are my Google messages that are to or from tevon@bruinen.co?")

# When creating a tool that has inputs, you'll either:
# 1. Need to pass a custom parameter parser function that will parse the input string into the correct format
# 2. Pass an LLM that will be used in the default parser

# How to deal with page tokens?
# We will need to do sequential calls to the Google API if we want to get all of the results
# This will likely need to be custom tool functionality, as we'll need to keep track of the page tokens and 
# keep calling the API until there's no next one


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
