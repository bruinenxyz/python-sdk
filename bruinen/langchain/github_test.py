import json
from typing import List, Optional

from pydantic import BaseModel, Field

from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.prompt import PromptTemplate
from langchain.tools import BaseTool

from ..bruinen_api_client import AuthenticatedClient
from ..bruinen_api_client.api.accounts import find_all_accounts_for_user
from ..bruinen_api_client.models import ReturnedAccountDto
from ..bruinen_api_client.types import Response

# Import input models (there aren't any for this one)

# Import the resource classes — in the generator we'll need to figure out how to include these names when there are multiple models


# TODO switch to using the created SDK class
class GithubGetReposInputSchema(BaseModel):
    name: Optional[str] = Field(description="Regex filter by name of repository")
    private: Optional[bool] = Field(description="Only return private users")


# TODO add output schema (also use the SDK class)
# class GithubGetReposOutputSchema(BaseModel):
#   ...


class GithubGetReposTool(BaseTool):
    name = "Github repos"
    # This is a description for any endpoint that has parameters created
    # description = """Gets a list of Github repos for a user.

    # Input should be a string query with the requested parameters as key/value pairs, separated by commas.
    # Possible keys for the query are:

    # "name": "string"
    # "private": "boolean"

    # If no parameters are provided, pass an empty string as input.

    # Output will be the text response from the Github API.
    # """
    # This is a description for any resource that doesn't have parameters
    description = """Gets a list of Github repos for a user.

    Input should be an empty string.

    Output will be the text response from the Github API.
    """

    llm: BaseLanguageModel
    user_id: str
    client: AuthenticatedClient

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        # TODO will need to switch to a different output parser once we use the generated SDK schema
        parser = PydanticOutputParser(pydantic_object=GithubGetReposInputSchema)

        prompt = PromptTemplate(
            template="Parse the provided input string. For values that are not marked as required, if no value is provided, return a null value.\n{format_instructions}\nHere is the input:\n{query}",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        _input = prompt.format_prompt(query=query)

        output = self.llm(_input.to_string())
        parser.parse(output)

        # TODO pass the parsed output to the Bruinen call

        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Github account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            print(account.source)
            if account.source == "github":
                account_id = account.id
        if account_id == "":
            # User has not authenticated Github, let the chain know to use the auth tool
            return "The user has not connected their Github account; you should try authenticating Github first."
        else:
            # User has authenticated Github, make the request
            from ..bruinen_api_client.api.sources import github_controller_profile
            from ..bruinen_api_client.models import GithubProfile

            response: Response[GithubProfile] = github_controller_profile.sync_detailed(
                client=self.client, account_id=account_id
            )
            if not 200 <= response.status_code < 300:
                return "Error pulling the user's Github profile."
            profile = response.parsed

            return json.dumps(profile.to_dict())

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))
