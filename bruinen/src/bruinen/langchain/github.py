# TODO figure out how the generator handles multiple methods (GET, POST, etc.) with the same name

import json
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.prompt import PromptTemplate
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import List, Optional

from ..client import AuthenticatedClient
from ..client.api.accounts import find_all_accounts_for_user
from ..client.api.auth import get_user_auth_token
from ..client.models import Auth, ReturnedAccountDto
from ..client.types import Response

from ..client.api.sources import github_controller_repos
from ..client.models import GithubRepo
from ..client.api.sources import github_controller_profile
from ..client.models import GithubProfile


class GithubAuthenticatorTool(BaseTool):
    name = 'Github Authenticator Tool'
    description = """Useful for when a user's Github account is not authenticated.
    Input to the tool should be an empty string.
    The response from the tool will be a URL that you return to the user for them to complete auth.
    """
    # Could add: This URL will be your final answer.

    client: AuthenticatedClient
    server: str
    user_id: str

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Run the tool."""
        response: Response[Auth] = get_user_auth_token(client=self.client, user_id=self.user_id)
        auth_token = json.loads(response.content)

        # TODO chat with Tevon about how this URL should be formatted
        return self.server + '?userToken=' + auth_token + '&source=github'

    # TODO implement this later
    async def _arun(
        self,
        user_id: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))



# Import input models (there aren't any for this one)

# Import the resource classes — in the generator we'll need to figure out how to include these names when there are multiple models



class GithubGetReposTool(BaseTool):
    name = "Github Get Repos Tool"
    # TODO add optionality, description to parameters
    description = """Useful for when you need to get a user's Github repos.
    
    Input should be an empty string.
    
    Output will be the text response from the Github API.
    """

    client: AuthenticatedClient
    user_id: str

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Github account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "github":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Github account; you should try authenticating Github first."
        else:
            # TODO pass additional parameters if required
            response: Response[List["GithubRepo"]] = github_controller_repos.sync_detailed(
                client=self.client,
                account_id=account_id
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Github repos."

             # Call each response item's to_dict() method and return the result as a JSON string
            return json.dumps(list(map(lambda x: x.to_dict(), response.parsed)))
            

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))



class GithubGetProfileTool(BaseTool):
    name = "Github Get Profile Tool"
    # TODO add optionality, description to parameters
    description = """Useful for when you need to get a user's Github profile.
    
    Input should be an empty string.
    
    Output will be the text response from the Github API.
    """

    client: AuthenticatedClient
    user_id: str

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Github account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "github":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Github account; you should try authenticating Github first."
        else:
            # TODO pass additional parameters if required
            response: Response[GithubProfile] = github_controller_profile.sync_detailed(
                client=self.client,
                account_id=account_id
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Github profile."

            return json.dumps(response.parsed)
            

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))

