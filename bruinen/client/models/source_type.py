from enum import Enum


class SourceType(str, Enum):
    AMAZON = "amazon"
    CASHAPP = "cashapp"
    DISCORD = "discord"
    DUNKIN = "dunkin"
    EMAIL = "email"
    ETHEREUM = "ethereum"
    FACEBOOK = "facebook"
    GCALENDAR = "gcalendar"
    GITHUB = "github"
    GMAIL = "gmail"
    GOOGLE = "google"
    LINKEDIN = "linkedin"
    POLYGON = "polygon"
    SHOPIFY = "shopify"
    SPOTIFY = "spotify"
    STACKOVERFLOW = "stackoverflow"
    TWITTER = "twitter"
    VENMO = "venmo"

    def __str__(self) -> str:
        return str(self.value)
