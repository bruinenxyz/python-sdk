# Bruinen secret for use in the SDK

bruinen_client_id = "24ab97c5-8f01-4a09-b5a5-e80743deb254"
bruinen_secret = "clg79qu20000muk22tlx0tybn"


# Create an authenticated client
from bruinen_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="http://localhost:3000", token=bruinen_secret)

# Find or create Tyler's email
from bruinen_api_client.models import ReturnedUserDto
from bruinen_api_client.api.default import users_controller_find_or_create_user
from bruinen_api_client.models import FindOrCreateUserDto
from bruinen_api_client.types import Response
from bruinen_api_client.api.default import confirm_controller_create
from bruinen_api_client.models import CreateConfirmDto

confirmation = confirm_controller_create(
    client=client,
    json_body=CreateConfirmDto.from_dict({"email": "tevon.strandbrown@gmail.com"}),
)

tyler_email = "tyler@bruinen.co"

request_object = FindOrCreateUserDto.from_dict({"email": tyler_email})
# request_object = FindOrCreateUserDto.from_dict({'email': tyler_email, 'clientId': bruinen_client_id })

response: Response[
    ReturnedUserDto
] = users_controller_find_or_create_user.sync_detailed(
    client=client, json_body=request_object
)
# print(response)

import json

user = json.loads(response.content)
print(user)

# from bruinen_api_client.models import Account
from bruinen_api_client.api.default import (
    accounts_controller_find_all_accounts_for_user,
)
from typing import List
from bruinen_api_client.models import ReturnedAccountDto


response: Response[
    List["ReturnedAccountDto"]
] = accounts_controller_find_all_accounts_for_user.sync_detailed(
    client=client, user_id=user["id"]
)

print(response)

# Figure out where we need to pass the access token or the user token

# See if we can organize by tag

# We should not return the Account field on the FindOrCreateUser from the OpenAPI schema, Grant is working on this now
# In the meantime for testing, can just update the api-json OpenAPI file to rmeove the account


# from bruinen_api_client.models import VenmoTransactions
# from bruinen_api_client.api.sources import venmo_controller_get_transactions
# from bruinen_api_client.types import Response


# response: Response[VenmoTransactions] = venmo_controller_get_transactions.sync_detailed(client=client, account_id=account_id)


# from bruinen-api-client.api_client import ApiClient


# def perform_query(self, query, email):
#         # If the user token isn't already set we'll need to find it, and pass it to the tools
#         if self.user_token == '':
#             secret = os.environ['BRUINEN_SECRET']
#             args = {
#                 'email': email
#             }
#             headers = {
#                 'Content-Type': 'application/json',
#                 'X-API-Key': secret
#             }

#             res_user = requests.post('https://api.bruinen.co/users/find-or-create', json=args, headers=headers)
#             self.user_id = res_user.json()['id']

#             res_token = requests.get(f'https://api.bruinen.co/auth/{self.user_id}', headers=headers)
#             self.user_token = res_token.json()['accessToken']

#             # Make sure to pass the ID and token to the classes that need them
#             for tool_class in self.tool_classes:
#                 tool_class.user_id = self.user_id
#             for auth_class in self.auth_classes:
#                 auth_class.user_token = self.user_token

#         llm = OpenAI(temperature=0)
#         agent = initialize_agent(self.tools, llm, agent='chat-zero-shot-react-description', verbose=True)
#         result = agent.run(query)

#         return result
