
Steps taken
Create a virtual environment
Install openAPI generator from https://github.com/openapi-generators/openapi-python-client:

pip install openapi-python-client

For tab completion:

openapi-python-client --install-completion

Generate the SDK from the OpenAPI specs (delete the previous bruinen-api-client folder if it exists):

openapi-python-client generate --path ./api-json

OR

openapi-python-client generate --url http://localhost:3000/api-json

Update the generated client.py file to include the following (changing to X-API-Key auth):

```python
@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    token: str
    prefix: str = ""
    auth_header_name: str = "X-API-Key"

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        auth_header_value = f"{self.prefix} {self.token}" if self.prefix else self.token
        return {self.auth_header_name: auth_header_value, **self.headers}
```

Install the SDK with:

pip install ./bruinen-api-client




Things to update:
Add a config file that overrides the class names
* Talk to Tevon about what these should look like
(remove the controller name)
* See if there's any additional structure that we need to add in — e.g., folders, etc.
* Do some testing to make sure that everything actually works 




Look at nestjs documentation for how nest auto-generates the name of each
Remove non-public API endpoints from the OpenAPI schema