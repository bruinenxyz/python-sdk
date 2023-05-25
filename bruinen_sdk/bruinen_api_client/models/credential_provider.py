from enum import Enum


class CredentialProvider(str, Enum):
    CLIENT = "client"
    PREFERUSER = "preferUser"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
