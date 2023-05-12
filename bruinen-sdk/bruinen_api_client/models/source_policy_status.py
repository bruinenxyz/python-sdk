from enum import Enum


class SourcePolicyStatus(str, Enum):
    ACTIVE = "active"
    DEACTIVATED = "deactivated"

    def __str__(self) -> str:
        return str(self.value)
