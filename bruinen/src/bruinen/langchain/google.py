# TODO figure out how the generator handles multiple methods (GET, POST, etc.) with the same name

import json
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.prompt import PromptTemplate
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Callable, List, Optional
from urllib.parse import quote

from ..client import AuthenticatedClient
from ..client.api.accounts import find_all_accounts_for_user
from ..client.api.auth import get_user_auth_token
from ..client.models import Auth, ReturnedAccountDto
from ..client.types import Response

from ..client.api.sources import google_controller_profile
from ..client.models import GoogleProfile
from ..client.api.sources import google_controller_drafts
from ..client.models import GoogleDrafts
from ..client.api.sources import google_controller_parsed_drafts
from ..client.models import GoogleParsedDrafts
from ..client.api.sources import google_controller_draft
from ..client.models import GoogleDraft
from ..client.api.sources import google_controller_parsed_draft
from ..client.models import GoogleParsedDraft
from ..client.api.sources import google_controller_labels
from ..client.models import GoogleLabels
from ..client.api.sources import google_controller_label
from ..client.models import GoogleLabel
from ..client.api.sources import google_controller_messages
from ..client.models import GoogleMessages
from ..client.api.sources import google_controller_parsed_messages
from ..client.models import GoogleParsedMessages
from ..client.api.sources import google_controller_message
from ..client.models import GoogleMessage
from ..client.api.sources import google_controller_parsed_message
from ..client.models import GoogleParsedMessage
from ..client.api.sources import google_controller_threads
from ..client.models import GoogleThreads
from ..client.api.sources import google_controller_parsed_threads
from ..client.models import GoogleParsedThreads
from ..client.api.sources import google_controller_thread
from ..client.models import GoogleThread
from ..client.api.sources import google_controller_parsed_thread
from ..client.models import GoogleParsedThread
from ..client.api.sources import google_controller_calendars
from ..client.models import GoogleCalendars
from ..client.api.sources import google_controller_calendar
from ..client.models import GoogleCalendar
from ..client.api.sources import google_controller_events
from ..client.models import GoogleEvents
from ..client.api.sources import google_controller_event
from ..client.models import GoogleEvent


class GoogleAuthenticatorTool(BaseTool):
    name = 'google_authenticator_tool'
    description = """Useful for when a user's Google account is not authenticated.

    Input to the tool should be an empty string.

    The response from the tool will be a URL that you return to the user for them to complete auth.
    The URL will be your final answer.
    """

    client: AuthenticatedClient
    user_id: str
    server: str = 'https://ui.bruinen.co'
    source_policy_id: str = None
    redirect_url: str

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Run the tool."""
        response: Response[Auth] = get_user_auth_token.sync_detailed(client=self.client, user_id=self.user_id)
        user_token = response.parsed.access_token

        if self.source_policy_id is not None:
            source = [{ 'name': 'google', 'sourcePolicyId': self.source_policy_id }]
        else:
            source = [{ 'name': 'google' }]
        encoded_source = quote(json.dumps(source))
        
        return self.server + '/connect' + '?userToken=' + quote(user_token) + '&sources=' + encoded_source + '&defaultRedirectUrl=' + quote(self.redirect_url)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetProfileTool(BaseTool):
    name = "google_get_profile_tool"
    description = """Useful for when you need to get a user's Google profile.
    
    Input should be the question that you want to know the answer to.
    
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    user_id: str
    parse_output: Optional[Callable[[GoogleProfile], str]] = None
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleProfile] = google_controller_profile.sync_detailed(
                client=self.client,
                account_id=account_id
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google profile."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetDraftsTool(BaseTool):
    name = "google_get_drafts_tool"
    description = """Useful for when you need to get a user's Google drafts.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetDraftsToolInputSchema(BaseModel):
        q: Optional[str] = Field(description="The query for your drafts")
        pageToken: Optional[str] = Field(description="The page token for your drafts")
        
    input_schema = GoogleGetDraftsToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetDraftsToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleDrafts], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetDraftsToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetDraftsToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleDrafts] = google_controller_drafts.sync_detailed(
                client=self.client,
                account_id=account_id,
                q=parsed_parameters.q,
                page_token=parsed_parameters.pageToken
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google drafts."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetParsedDraftsTool(BaseTool):
    name = "google_get_parsed_drafts_tool"
    description = """Useful for when you need to get a user's Google parsed_drafts.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetParsedDraftsToolInputSchema(BaseModel):
        q: Optional[str] = Field(description="The query for your drafts")
        pageToken: Optional[str] = Field(description="The page token for your drafts")
        
    input_schema = GoogleGetParsedDraftsToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetParsedDraftsToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleParsedDrafts], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetParsedDraftsToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetParsedDraftsToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleParsedDrafts] = google_controller_parsed_drafts.sync_detailed(
                client=self.client,
                account_id=account_id,
                q=parsed_parameters.q,
                page_token=parsed_parameters.pageToken
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google parsed_drafts."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetDraftTool(BaseTool):
    name = "google_get_draft_tool"
    description = """Useful for when you need to get a user's Google draft.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetDraftToolInputSchema(BaseModel):
        draftId: str = Field(description="The id of the draft")
        
    input_schema = GoogleGetDraftToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetDraftToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleDraft], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetDraftToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetDraftToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleDraft] = google_controller_draft.sync_detailed(
                client=self.client,
                account_id=account_id,
                draft_id=parsed_parameters.draftId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google draft."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetParsedDraftTool(BaseTool):
    name = "google_get_parsed_draft_tool"
    description = """Useful for when you need to get a user's Google parsed_draft.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetParsedDraftToolInputSchema(BaseModel):
        draftId: str = Field(description="The id of the draft")
        
    input_schema = GoogleGetParsedDraftToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetParsedDraftToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleParsedDraft], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetParsedDraftToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetParsedDraftToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleParsedDraft] = google_controller_parsed_draft.sync_detailed(
                client=self.client,
                account_id=account_id,
                draft_id=parsed_parameters.draftId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google parsed_draft."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetLabelsTool(BaseTool):
    name = "google_get_labels_tool"
    description = """Useful for when you need to get a user's Google labels.
    
    Input should be the question that you want to know the answer to.
    
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    user_id: str
    parse_output: Optional[Callable[[GoogleLabels], str]] = None
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleLabels] = google_controller_labels.sync_detailed(
                client=self.client,
                account_id=account_id
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google labels."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetLabelTool(BaseTool):
    name = "google_get_label_tool"
    description = """Useful for when you need to get a user's Google label.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetLabelToolInputSchema(BaseModel):
        labelId: str = Field(description="The id of the label")
        
    input_schema = GoogleGetLabelToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetLabelToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleLabel], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetLabelToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetLabelToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleLabel] = google_controller_label.sync_detailed(
                client=self.client,
                account_id=account_id,
                label_id=parsed_parameters.labelId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google label."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetMessagesTool(BaseTool):
    name = "google_get_messages_tool"
    description = """Useful for when you need to get a user's Google messages.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetMessagesToolInputSchema(BaseModel):
        q: Optional[str] = Field(description="The query of the messages")
        pageToken: Optional[str] = Field(description="The pageToken of the messages")
        labelIds: Optional[str] = Field(description="The labelIds of the messages")
        
    input_schema = GoogleGetMessagesToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetMessagesToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleMessages], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetMessagesToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetMessagesToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleMessages] = google_controller_messages.sync_detailed(
                client=self.client,
                account_id=account_id,
                q=parsed_parameters.q,
                page_token=parsed_parameters.pageToken,
                label_ids=parsed_parameters.labelIds
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google messages."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetParsedMessagesTool(BaseTool):
    name = "google_get_parsed_messages_tool"
    description = """Useful for when you need to get a user's Google parsed_messages.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetParsedMessagesToolInputSchema(BaseModel):
        q: Optional[str] = Field(description="The query of the messages")
        pageToken: Optional[str] = Field(description="The pageToken of the messages")
        labelIds: Optional[str] = Field(description="The labelIds of the messages")
        
    input_schema = GoogleGetParsedMessagesToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetParsedMessagesToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleParsedMessages], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetParsedMessagesToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetParsedMessagesToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleParsedMessages] = google_controller_parsed_messages.sync_detailed(
                client=self.client,
                account_id=account_id,
                q=parsed_parameters.q,
                page_token=parsed_parameters.pageToken,
                label_ids=parsed_parameters.labelIds
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google parsed_messages."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetMessageTool(BaseTool):
    name = "google_get_message_tool"
    description = """Useful for when you need to get a user's Google message.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetMessageToolInputSchema(BaseModel):
        messageId: str = Field(description="The id of the message")
        
    input_schema = GoogleGetMessageToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetMessageToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleMessage], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetMessageToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetMessageToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleMessage] = google_controller_message.sync_detailed(
                client=self.client,
                account_id=account_id,
                message_id=parsed_parameters.messageId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google message."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetParsedMessageTool(BaseTool):
    name = "google_get_parsed_message_tool"
    description = """Useful for when you need to get a user's Google parsed_message.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetParsedMessageToolInputSchema(BaseModel):
        messageId: str = Field(description="The id of the message")
        
    input_schema = GoogleGetParsedMessageToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetParsedMessageToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleParsedMessage], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetParsedMessageToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetParsedMessageToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleParsedMessage] = google_controller_parsed_message.sync_detailed(
                client=self.client,
                account_id=account_id,
                message_id=parsed_parameters.messageId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google parsed_message."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetThreadsTool(BaseTool):
    name = "google_get_threads_tool"
    description = """Useful for when you need to get a user's Google threads.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetThreadsToolInputSchema(BaseModel):
        q: Optional[str] = Field(description="The query of the threads")
        pageToken: Optional[str] = Field(description="The pageToken of the threads")
        labelIds: Optional[str] = Field(description="The labelIds of the threads")
        
    input_schema = GoogleGetThreadsToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetThreadsToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleThreads], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetThreadsToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetThreadsToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleThreads] = google_controller_threads.sync_detailed(
                client=self.client,
                account_id=account_id,
                q=parsed_parameters.q,
                page_token=parsed_parameters.pageToken,
                label_ids=parsed_parameters.labelIds
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google threads."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetParsedThreadsTool(BaseTool):
    name = "google_get_parsed_threads_tool"
    description = """Useful for when you need to get a user's Google parsed_threads.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetParsedThreadsToolInputSchema(BaseModel):
        q: Optional[str] = Field(description="The query of the threads")
        pageToken: Optional[str] = Field(description="The pageToken of the threads")
        labelIds: Optional[str] = Field(description="The labelIds of the threads")
        
    input_schema = GoogleGetParsedThreadsToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetParsedThreadsToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleParsedThreads], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetParsedThreadsToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetParsedThreadsToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleParsedThreads] = google_controller_parsed_threads.sync_detailed(
                client=self.client,
                account_id=account_id,
                q=parsed_parameters.q,
                page_token=parsed_parameters.pageToken,
                label_ids=parsed_parameters.labelIds
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google parsed_threads."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetThreadTool(BaseTool):
    name = "google_get_thread_tool"
    description = """Useful for when you need to get a user's Google thread.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetThreadToolInputSchema(BaseModel):
        threadId: str = Field(description="The id of the thread")
        
    input_schema = GoogleGetThreadToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetThreadToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleThread], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetThreadToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetThreadToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleThread] = google_controller_thread.sync_detailed(
                client=self.client,
                account_id=account_id,
                thread_id=parsed_parameters.threadId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google thread."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetParsedThreadTool(BaseTool):
    name = "google_get_parsed_thread_tool"
    description = """Useful for when you need to get a user's Google parsed_thread.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetParsedThreadToolInputSchema(BaseModel):
        threadId: str = Field(description="The id of the thread")
        
    input_schema = GoogleGetParsedThreadToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetParsedThreadToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleParsedThread], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetParsedThreadToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetParsedThreadToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleParsedThread] = google_controller_parsed_thread.sync_detailed(
                client=self.client,
                account_id=account_id,
                thread_id=parsed_parameters.threadId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google parsed_thread."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetCalendarsTool(BaseTool):
    name = "google_get_calendars_tool"
    description = """Useful for when you need to get a user's Google calendars.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetCalendarsToolInputSchema(BaseModel):
        syncToken: Optional[str] = Field(description="The syncToken of the calendars")
        showHidden: Optional[bool] = Field(description="Whether to show hidden calendars")
        showDeleted: Optional[bool] = Field(description="Whether to show deleted calendars")
        pageToken: Optional[str] = Field(description="The pageToken of the calendars")
        
    input_schema = GoogleGetCalendarsToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetCalendarsToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleCalendars], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetCalendarsToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetCalendarsToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleCalendars] = google_controller_calendars.sync_detailed(
                client=self.client,
                account_id=account_id,
                sync_token=parsed_parameters.syncToken,
                show_hidden=parsed_parameters.showHidden,
                show_deleted=parsed_parameters.showDeleted,
                page_token=parsed_parameters.pageToken
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google calendars."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetCalendarTool(BaseTool):
    name = "google_get_calendar_tool"
    description = """Useful for when you need to get a user's Google calendar.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetCalendarToolInputSchema(BaseModel):
        calendarId: str = Field(description="The id of the calendar")
        
    input_schema = GoogleGetCalendarToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetCalendarToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleCalendar], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetCalendarToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetCalendarToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleCalendar] = google_controller_calendar.sync_detailed(
                client=self.client,
                account_id=account_id,
                calendar_id=parsed_parameters.calendarId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google calendar."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetEventsTool(BaseTool):
    name = "google_get_events_tool"
    description = """Useful for when you need to get a user's Google events.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetEventsToolInputSchema(BaseModel):
        iCalUID: Optional[str] = Field(description="The iCal UID")
        syncToken: Optional[str] = Field(description="The sync token")
        updatedMin: Optional[str] = Field(description="The updated min")
        timeZone: Optional[str] = Field(description="The time zone")
        timeMin: Optional[str] = Field(description="The time min")
        timeMax: Optional[str] = Field(description="The time max")
        singleEvents: Optional[bool] = Field(description="Whether to show single events")
        showDeleted: Optional[bool] = Field(description="Whether to show deleted")
        q: Optional[str] = Field(description="The query")
        pageToken: Optional[str] = Field(description="The page token")
        orderBy: Optional[str] = Field(description="The order by")
        maxAttendees: Optional[int] = Field(description="The max attendees")
        calendarId: Optional[str] = Field(description="The id of the calendar")
        
    input_schema = GoogleGetEventsToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetEventsToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleEvents], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetEventsToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetEventsToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleEvents] = google_controller_events.sync_detailed(
                client=self.client,
                account_id=account_id,
                i_cal_uid=parsed_parameters.iCalUID,
                sync_token=parsed_parameters.syncToken,
                updated_min=parsed_parameters.updatedMin,
                time_zone=parsed_parameters.timeZone,
                time_min=parsed_parameters.timeMin,
                time_max=parsed_parameters.timeMax,
                single_events=parsed_parameters.singleEvents,
                show_deleted=parsed_parameters.showDeleted,
                q=parsed_parameters.q,
                page_token=parsed_parameters.pageToken,
                order_by=parsed_parameters.orderBy,
                max_attendees=parsed_parameters.maxAttendees,
                calendar_id=parsed_parameters.calendarId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google events."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)


class GoogleGetEventTool(BaseTool):
    name = "google_get_event_tool"
    description = """Useful for when you need to get a user's Google event.
    
    Input should be a string containing the question that you want to know the answer to.
    Do not pass parameters as JSON, instead pass the string to the tool as is.
    
    Output will be the text response from the Google API.
    """

    class GoogleGetEventToolInputSchema(BaseModel):
        timeZone: Optional[str] = Field(description="The timeZone of the event")
        eventId: str = Field(description="The id of the event")
        calendarId: str = Field(description="The calendarId of the calendar which contains the event")
        
    input_schema = GoogleGetEventToolInputSchema

    client: AuthenticatedClient
    user_id: str
    llm: Optional[BaseLanguageModel]
    parse_parameters: Optional[Callable[[str], GoogleGetEventToolInputSchema]] = None
    parse_output: Optional[Callable[[GoogleEvent], str]] = None
    
    def _parse_parameters(self, _query: str) -> GoogleGetEventToolInputSchema:
        """Parse the input passed to the tool when running."""
        parser = PydanticOutputParser(pydantic_object=self.GoogleGetEventToolInputSchema)
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
        if self.llm is None:
            return "Error: No language model provided for input parsing."
        output = self.llm(_input.to_string())
        return parser.parse(output)
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""
        
        # If no custom input parameter parser is passed, use the default one
        if self.parse_parameters is None:
            parsed_parameters = self._parse_parameters(query)
        else: 
            parsed_parameters = self.parse_parameters(query)
        
        response: Response[List["ReturnedAccountDto"]] = find_all_accounts_for_user.sync_detailed(
            client=self.client, user_id=self.user_id
        )
        if not 200 <= response.status_code < 300:
            return "Error pulling the user's Google account."
        accounts: List["ReturnedAccountDto"] = response.parsed

        account_id = ""
        for account in accounts:
            if account.source == "google":
                account_id = account.id
        if account_id == "":
            return "The user has not connected their Google account; you should try authenticating Google first."
        else:
            response: Response[GoogleEvent] = google_controller_event.sync_detailed(
                client=self.client,
                account_id=account_id,
                time_zone=parsed_parameters.timeZone,
                event_id=parsed_parameters.eventId,
                calendar_id=parsed_parameters.calendarId
            )
            if not 200 <= response.status_code < 300:
                return "Error when attempting to get the user's Google event."

            if self.parse_output is None:
                return json.dumps(response.parsed.to_dict())
            else:
                return self.parse_output(response.parsed, query)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self._run(query, run_manager)

