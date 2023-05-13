from jinja2 import Template

# Load the template from the file
with open("templates/tool_template.jinja2") as f:
    template = Template(f.read())

# Define the data to use in the template
data = {
    "controller_name": "MyController",
    "methods": {
        "get": {
            "parameters": [
                {"name": "id", "type": "str"},
            ],
        },
        "put": {
            "parameters": [
                {"name": "id", "type": "str"},
                {"name": "data", "type": "dict"},
            ],
        },
    },
}

# Render the template with the data
result = template.render(data)

# Print the result
print(result)


# Notes on tools

# Each tool should have:
#   A name
#   A description
#   function(input: string)
#     parser ----  Parser(Pydantic(Resource.InputType))
#       InputType can come from the JSON schema
#       The parser can come from LangChain
#     API call
#   Response should be the string response from the API

# - We should also build a Langchain authenticator
#     - SDK should take as config a Bruinen server instance
#         - Either the client should be running their own server (if they’re running their own server with our open source code), or it will be our server
#     - It will need the client’s API key and the server URL
#     - For now have it return a link like my tool did, and in the future could be an embeddable component, react component, HTML, magic link, etc.
# - Go to the hosted URL — Tevon to send through


# On the base source class in Tevon's repo
# Make a function that returns a JSON representation of the source
#   Source name, definition, type (oauth2, etc.)
#   For each resource, name, description, input type, output type
# Then for each of those we'll have a tool that combines the definition of the source and the definition of the resource
# Then creates a parser for the input type and output type

# Should use Tevon's source repo to help define these tools

# For the interim, we should do this where the SDK and the langchain tool generator are generated separately
#   The SDK will be generated from the OpenAPI spec
#   The langchain tool generator will be generated from the source repo
