from enum import Enum


class ClientCredentialType(str, Enum):
    APIKEY = "APIKey"
    OAUTH2 = "OAuth2"

    def __str__(self) -> str:
        return str(self.value)
