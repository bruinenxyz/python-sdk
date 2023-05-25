from enum import Enum


class AccountStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
