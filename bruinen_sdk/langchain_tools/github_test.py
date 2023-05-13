# This file defines the example of a generated Github Repo tool, as well as the autneticator tool
# Things that we need to do still:
#   x Remove the user ID as a parameter and switch it to being passed on initialization
#   - Update the tool to not parse the output if no parameters are passed in
#   x Import the Bruinen SDK
#   x Use the Bruinen SDK to pull the user's list of accounts
#   x Check if the Github account is listed in those accounts; if not, generate a connect URL
#   - If the Github account is listed, then use the account ID to make the request
#   - Add the CallbackManagerForToolRun functionality (maybe)
#   - Generate output model in Pydantic


import json
from typing import List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.prompt import PromptTemplate
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

from ..bruinen_api_client import AuthenticatedClient
from ..bruinen_api_client.api.accounts import find_all_accounts_for_user
from ..bruinen_api_client.models import ReturnedAccountDto
from ..bruinen_api_client.types import Response


# Define the desired data structure for input to the LLM
# TODO add optionality to this
class GithubGetReposInputSchema(BaseModel):
    name: Optional[str] = Field(description="Regex filter by name of repository")
    private: Optional[bool] = Field(description="Only return private users")


# TODO define the output schema based on the JSON schema input
# class GithubGetReposOutputSchema(BaseModel):
#   ...


class GithubGetReposTool(BaseTool):
    name = "Github repos"
    # This is a description for any endpoint that has parameters created
    description = """Gets a list of Github repos for a user.
    
    Input should be a string query with the requested parameters as key/value pairs, separated by commas.
    Possible keys for the query are:
    
    "name": "string"
    "private": "boolean"

    If no parameters are provided, pass an empty string as input.
    
    Output will be the text response from the Github API.
    """
    # This is a description for any resource that doesn't have parameters
    # description = '''Gets a list of Github repos for a user.

    # Input should be an empty string.

    # Output will be the text response from the Github API.
    # '''

    llm: BaseLanguageModel
    user_id: str
    client: AuthenticatedClient

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        # TODO the generated version should not take an LLM as input since it isn't necessary
        # and the code below should not have any logic around the LLM

        parser = PydanticOutputParser(pydantic_object=GithubGetReposInputSchema)

        # TODO figure out how to deal with optional values gracefully — return a null value?
        prompt = PromptTemplate(
            template="Parse the provided input string. For values that are not marked as required, if no value is provided, return a null value.\n{format_instructions}\nHere is the input:\n{query}",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        _input = prompt.format_prompt(query=query)

        print(_input.to_string())
        output = self.llm(_input.to_string())
        fields = parser.parse(output)

        print("fields")
        print(fields)

        # return ''
        # Get the list of user accounts and check if the Github accounts is provided
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        accounts = json.loads(response.content)
        # Might have to add another step in here
        account_id = ""
        for account in accounts:
            if account["source"] == "github":
                account_id = account["id"]
        if account_id == "":
            # User has not authenticated Github, let the chain know to use the auth tool
            return "The user has not connected their Github account; you should try authenticating Github first."
        else:
            # TODO implement this once the python SDK has sources included
            # If the user is authenticated, then we can use the account ID to make the request
            # res_repos = requests.get(f'https://api.bruinen.co/sources/github/repos?accountId={account_id}', headers=headers)
            # repos = res_repos.json()

            return ""

    # TODO implement this later
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GithubAuthenticator(BaseTool):
    name = "Github authenticator"
    description = """Userful for when a user\'s Github account is not authenticated.
    Input to the tool should be a string with the user's Bruinen user ID.
    The response from the tool will be a URL that you return to the user for them to complete auth.
    """
    # Could add: This URL will be your final answer.

    # client: BruinenAuthenticatedClient

    def _run(self, user_id: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        # Use this to generate a Connect URL if we need the chain to authenticate a user's account
        # res_token = requests.get(f'https://api.bruinen.co/auth/{self.user_id}', headers=headers)
        # self.user_token = res_token.json()['accessToken']

        # def generateConnectUrl(user_token, source):
        #     connect_base = 'http://localhost:3001/'
        #     connect_url = connect_base + '?userToken=' + user_token + '&source=' + source

        #     return connect_url
        return ""

    # TODO implement this later
    async def _arun(
        self,
        user_id: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


# Below is my attempt to create the tool without the LLM that parses input.
# Not working very well at the moment

# class GithubGetReposTool(BaseTool):
#     name = 'Github repos'
#     description = '''Gets a list of Github repos for a user.

#     Input should be a JSON string with one key: "data".
#     The value of "data" should be a dictionary of
#     key-value pairs that you want to use as parameters to the request to Github.

#     The format of the input is below:
#     ```
#     {
#         "data": {
#             "userId": "string",
#             "name": "string",
#             "private": "boolean"
#         }
#     }
#     ```

#     All of the keys in "data" are optional. If you don't provide a key, it will not be used in the request.

#     Be careful to always use double quotes for strings in the JSON string.

#     Output will be the text response from the Github API.
#     '''


#     # """Use this when you want to POST to a website.
#     # Input should be a json string with two keys: "url" and "data".
#     # The value of "url" should be a string, and the value of "data" should be a dictionary of
#     # key-value pairs you want to POST to the url.
#     # Be careful to always use double quotes for strings in the json string
#     # The output will be the text response of the POST request.
#     # """

#     llm: BaseLanguageModel

#     def _run(
#         self,
#         text: str,
#         run_manager: Optional[CallbackManagerForToolRun] = None
#     ) -> str:
#         '''Run the tool.'''

#         # parser = PydanticOutputParser(pydantic_object=GithubQuerySchema)
#         text_json = json.loads(text)
#         print(text_json)

#         return ''

#     async def _arun(
#         self,
#         text: str,
#         run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
#     ) -> str:
#         """Run the tool asynchronously."""
#         return await self.requests_wrapper.aget((text))
