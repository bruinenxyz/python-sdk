# TODO figure out how the generator handles multiple methods (GET, POST, etc.) with the same name

import json
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.prompt import PromptTemplate
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Callable, List, Optional

from ..client import AuthenticatedClient
from ..client.api.accounts import find_all_accounts_for_user
from ..client.api.auth import get_user_auth_token
from ..client.models import Auth, ReturnedAccountDto
from ..client.types import Response

from ..client.api.sources import google_controller_profile
from ..client.models import GoogleProfile
from ..client.api.sources import google_controller_drafts
from ..client.models import GoogleDrafts
from ..client.api.sources import google_controller_draft
from ..client.models import GoogleDraft
from ..client.api.sources import google_controller_labels
from ..client.models import GoogleLabels
from ..client.api.sources import google_controller_label
from ..client.models import GoogleLabel
from ..client.api.sources import google_controller_messages
from ..client.models import GoogleMessages
from ..client.api.sources import google_controller_message
from ..client.models import GoogleMessage
from ..client.api.sources import google_controller_threads
from ..client.models import GoogleThreads
from ..client.api.sources import google_controller_thread
from ..client.models import GoogleThread
from ..client.api.sources import google_controller_calendars
from ..client.models import GoogleCalendars
from ..client.api.sources import google_controller_calendar
from ..client.models import GoogleCalendar
from ..client.api.sources import google_controller_events
from ..client.models import GoogleEvents
from ..client.api.sources import google_controller_event
from ..client.models import GoogleEvent


class GoogleAuthenticatorTool(BaseTool):
    name = 'Google Authenticator Tool'
    description = """Useful for when a user's Google account is not authenticated.

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
        return self.server + '?userToken=' + auth_token + '&source=google'

    # TODO implement this later
    async def _arun(
        self,
        user_id: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetProfileTool(BaseTool):
    name = "Google Get Profile Tool"
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
        return await self.requests_wrapper.aget((query))


class GoogleGetDraftsTool(BaseTool):
    name = "Google Get Drafts Tool"
    description = """Useful for when you need to get a user's Google drafts.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "q" (Optional), string: "The query for your drafts"
    "pageToken" (Optional), string: "The page token for your drafts"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleDrafts], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetDraftsToolInputSchema(BaseModel):
            q: Optional[str] = Field(description="The query for your drafts")
            pageToken: Optional[str] = Field(description="The page token for your drafts")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetDraftsToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetDraftTool(BaseTool):
    name = "Google Get Draft Tool"
    description = """Useful for when you need to get a user's Google draft.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "draftId" (Required), string: "The id of the draft"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleDraft], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetDraftToolInputSchema(BaseModel):
            draftId: str = Field(description="The id of the draft")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetDraftToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetLabelsTool(BaseTool):
    name = "Google Get Labels Tool"
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
        return await self.requests_wrapper.aget((query))


class GoogleGetLabelTool(BaseTool):
    name = "Google Get Label Tool"
    description = """Useful for when you need to get a user's Google label.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "labelId" (Required), string: "The id of the label"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleLabel], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetLabelToolInputSchema(BaseModel):
            labelId: str = Field(description="The id of the label")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetLabelToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetMessagesTool(BaseTool):
    name = "Google Get Messages Tool"
    description = """Useful for when you need to get a user's Google messages.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "q" (Optional), string: "The query of the messages"
    "pageToken" (Optional), string: "The pageToken of the messages"
    "labelIds" (Optional), string: "The labelIds of the messages"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleMessages], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetMessagesToolInputSchema(BaseModel):
            q: Optional[str] = Field(description="The query of the messages")
            pageToken: Optional[str] = Field(description="The pageToken of the messages")
            labelIds: Optional[str] = Field(description="The labelIds of the messages")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetMessagesToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetMessageTool(BaseTool):
    name = "Google Get Message Tool"
    description = """Useful for when you need to get a user's Google message.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "messageId" (Required), string: "The id of the message"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleMessage], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetMessageToolInputSchema(BaseModel):
            messageId: str = Field(description="The id of the message")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetMessageToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetThreadsTool(BaseTool):
    name = "Google Get Threads Tool"
    description = """Useful for when you need to get a user's Google threads.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "q" (Optional), string: "The query of the threads"
    "pageToken" (Optional), string: "The pageToken of the threads"
    "labelIds" (Optional), string: "The labelIds of the threads"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleThreads], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetThreadsToolInputSchema(BaseModel):
            q: Optional[str] = Field(description="The query of the threads")
            pageToken: Optional[str] = Field(description="The pageToken of the threads")
            labelIds: Optional[str] = Field(description="The labelIds of the threads")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetThreadsToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetThreadTool(BaseTool):
    name = "Google Get Thread Tool"
    description = """Useful for when you need to get a user's Google thread.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "threadId" (Required), string: "The id of the thread"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleThread], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetThreadToolInputSchema(BaseModel):
            threadId: str = Field(description="The id of the thread")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetThreadToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetCalendarsTool(BaseTool):
    name = "Google Get Calendars Tool"
    description = """Useful for when you need to get a user's Google calendars.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "syncToken" (Optional), string: "The syncToken of the calendars"
    "showHidden" (Optional), boolean: "Whether to show hidden calendars"
    "showDeleted" (Optional), boolean: "Whether to show deleted calendars"
    "pageToken" (Optional), string: "The pageToken of the calendars"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleCalendars], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetCalendarsToolInputSchema(BaseModel):
            syncToken: Optional[str] = Field(description="The syncToken of the calendars")
            showHidden: Optional[bool] = Field(description="Whether to show hidden calendars")
            showDeleted: Optional[bool] = Field(description="Whether to show deleted calendars")
            pageToken: Optional[str] = Field(description="The pageToken of the calendars")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetCalendarsToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetCalendarTool(BaseTool):
    name = "Google Get Calendar Tool"
    description = """Useful for when you need to get a user's Google calendar.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "calendarId" (Required), string: "The id of the calendar"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleCalendar], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetCalendarToolInputSchema(BaseModel):
            calendarId: str = Field(description="The id of the calendar")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetCalendarToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetEventsTool(BaseTool):
    name = "Google Get Events Tool"
    description = """Useful for when you need to get a user's Google events.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "iCalUID" (Optional), string: "The iCal UID"
    "syncToken" (Optional), string: "The sync token"
    "updatedMin" (Optional), string: "The updated min"
    "timeZone" (Optional), string: "The time zone"
    "timeMin" (Optional), string: "The time min"
    "timeMax" (Optional), string: "The time max"
    "singleEvents" (Optional), boolean: "Whether to show single events"
    "showDeleted" (Optional), boolean: "Whether to show deleted"
    "q" (Optional), string: "The query"
    "pageToken" (Optional), string: "The page token"
    "orderBy" (Optional), string: "The order by"
    "maxAttendees" (Optional), number: "The max attendees"
    "calendarId" (Optional), string: "The id of the calendar"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleEvents], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

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
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetEventsToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))


class GoogleGetEventTool(BaseTool):
    name = "Google Get Event Tool"
    description = """Useful for when you need to get a user's Google event.
    
    The input should be a string with two parts, separated by a new line.

    The first line should be the question that you want to know the answer to.

    The second line should be the requested parameters to the Google API, as key/value pairs, separated by commas. 
    For keys that are not marked as required, if no value is provided, do not include the key.
    Possible keys for the the second line are:
    
    "timeZone" (Optional), string: "The timeZone of the event"
    "eventId" (Required), string: "The id of the event"
    "calendarId" (Required), string: "The calendarId of the calendar which contains the event"
    
    If no parameters are provided, pass "No parameters" as the second line.
    Output will be the text response from the Google API.
    """

    client: AuthenticatedClient
    llm: BaseLanguageModel
    user_id: str
    parse_output: Optional[Callable[[GoogleEvent], str]] = None

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Run the tool."""

        class GoogleGetEventToolInputSchema(BaseModel):
            timeZone: Optional[str] = Field(description="The timeZone of the event")
            eventId: str = Field(description="The id of the event")
            calendarId: str = Field(description="The calendarId of the calendar which contains the event")
            
        question, raw_parameters = query.split("\n", 1)
        
        parser = PydanticOutputParser(pydantic_object=GoogleGetEventToolInputSchema)
        
        prompt = PromptTemplate(
            template="""Parse the provided input string.
            For values that are not marked as required, if no value is provided, return a null value.
            {format_instructions}
            Here is the input:
            {query}""",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        _input = prompt.format_prompt(query=raw_parameters)
        output = self.llm(_input.to_string())
        parsed_parameters = parser.parse(output)
        
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
                return self.parse_output(response.parsed, question)

    # TODO implement async version
    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        return await self.requests_wrapper.aget((query))

