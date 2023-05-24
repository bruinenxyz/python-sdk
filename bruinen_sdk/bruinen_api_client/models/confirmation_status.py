from enum import Enum


class ConfirmationStatus(str, Enum):
    CONFIRMED = "confirmed"
    DELIVERED = "delivered"
    DENIED = "denied"
    ERROR = "error"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
