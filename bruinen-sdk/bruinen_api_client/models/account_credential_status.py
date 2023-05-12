from enum import Enum


class AccountCredentialStatus(str, Enum):
    ACTIVE = "active"
    DEACTIVATED = "deactivated"

    def __str__(self) -> str:
        return str(self.value)
