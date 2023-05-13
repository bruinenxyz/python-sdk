# from bruinen_sdk.confirm import confirm_action
from bruinen_sdk.confirm.confirm import confirm_action


def on_reject():
    print("THEY REJECTED THE ACTION")


@confirm_action(
    "test",
    "magic-link",
    delivery_address="tevon.strandbrown@gmail.com",
    on_reject=on_reject,
    on_magic_link=lambda x: print(x),
)
def test():
    print("SUCCESS! THEY CONFIRMED THE ACTION")


test()
# def test2():
#     print("TEST 2")
#     pendulum.now()
