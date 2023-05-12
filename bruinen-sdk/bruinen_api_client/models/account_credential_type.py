from enum import Enum


class AccountCredentialType(str, Enum):
    APIKEY = "APIKey"
    OAUTH2 = "OAuth2"
    PUPPETEERCOOKIES = "PuppeteerCookies"

    def __str__(self) -> str:
        return str(self.value)
