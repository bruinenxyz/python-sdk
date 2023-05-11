# Getting started

Currently only supports a single decorator method, `confirm_action`.

See `confirm_example.py` for example usage.

Supported values for `delivery_channel`: `email`, `sms`, `magic-link`

`email` - expected `delivery_address` to be a full email
`sms` - expects `delivery_address` to be a full phone number, beginning with `+1` or whatever the country code is.
`magic-link` - does not require a delivery_address. It will call `on_magic_link` callback if provided, with a dict containing `magicLinkUrl, confirmationId, delivered`

Decorating a function will `confirm_action` will prevent it from being run until the user has confirmed the action. There is currently not timeout.
If the user denies the action, the `on_rejected` function will be called. If the user accepts the action, the function will be called normally.

### Configuration
The library depends on two environment variables:

`BRUINEN_API_KEY`: your Bruinen API key for accessing the API
`BRUINEN_API_URL`: the base URL for the Bruinen server you will be using