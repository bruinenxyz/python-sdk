# This should be a test file that shows a proof of concept on how to use the SDK and Langchain tools to run an agent and ask a query
# Things that we need to add:
#   x Importing the SDK and setting it up
#   - Create a chain with the Github authentication tool and resource tools
#   - Run the chain and use the Pydantic output model to format the result

import os

from dotenv import load_dotenv

load_dotenv()

bruinen_client_id = os.getenv("BRUINEN_CLIENT_ID")
bruinen_secret = os.getenv("BRUINEN_SECRET")
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# # TODO switch to the generated version
from bruinen_sdk.langchain_tools.github_test import GithubGetReposTool

from bruinen_sdk.bruinen_api_client import AuthenticatedClient

bruinen_secret = os.environ["BRUINEN_SECRET"]
bruinen_client_id = os.environ["BRUINEN_CLIENT_ID"]

client = AuthenticatedClient(base_url="http://localhost:3000", token=bruinen_secret)

# TODO remove
user_id = "asd"

from bruinen_sdk.bruinen_api_client.models import UpsertUserDto, ReturnedUserDto

from bruinen_sdk.bruinen_api_client.api.default import (
    users_controller_find_or_create_user,
)
from bruinen_sdk.bruinen_api_client.types import Response

# # TODO: check for the SDK whether we should tag the users controller stuff with 'user'

tyler_email = "tyler@bruinen.co"

request_object = UpsertUserDto.from_dict(
    {"email": tyler_email, "clientId": bruinen_client_id}
)
response: Response[
    ReturnedUserDto
] = users_controller_find_or_create_user.sync_detailed(
    client=client, json_body=request_object
)

print(response)

llm = OpenAI(temperature=0)

github = GithubGetReposTool(llm=llm, client=client, user_id=user_id)

agent = initialize_agent(
    [github], llm, agent="chat-zero-shot-react-description", verbose=True
)
result = agent.run("What are my Github repos?")
