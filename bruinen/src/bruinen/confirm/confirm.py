# Create an authenticated client
import os
from functools import wraps
from time import sleep

from ..client import AuthenticatedClient

token = os.environ.get("BRUINEN_API_KEY")
base_url = os.environ.get("BRUINEN_API_URL")

client = AuthenticatedClient(
    base_url=base_url or "http://localhost:3000",
    token=token,
    prefix="",
    auth_header_name="X-API-Key",
)

from ..client.api.confirm import create as confirm_create
from ..client.api.confirm import find_one as confirm_get
from ..client.models import CreateConfirmDto


def confirm_action(
    action,
    delivery_channel,
    params={},
    delivery_address=None,
    on_reject=None,
    on_magic_link=None,
):
    """confirm an action before calling function"""

    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            confirmation = confirm_create.sync(
                client=client,
                json_body=CreateConfirmDto.from_dict(
                    {
                        "type": "test",
                        "deliveryAddress": delivery_address,
                        "deliveryChannel": delivery_channel,
                        "action": action,
                        "params": params,
                    }
                ),
            )
            if delivery_channel == "magic-link":
                if on_magic_link:
                    on_magic_link(confirmation.to_dict())
            conf = None
            while True:
                print("Checking for confirmation")
                conf = confirm_get.sync(client=client, id=confirmation.confirmation_id)
                conf = conf.to_dict()
                print(conf)
                if "respondedAt" in conf:
                    break
                sleep(3)
            if conf["status"] == "denied":
                if on_reject:
                    on_reject()
                return
            if conf["status"] == "confirmed":
                fn(*args, **kwargs)
                return

        return wrapper

    return decorate
