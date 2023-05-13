from jinja2 import Template
from typing import List, Dict, Union
import json

# TODO change naming once it's updated
# TODO add description to JSON generated, e.g.
# tool_description = 'Get a list of Github repos for a user'


with open('templates/resource_tool_template.jinja2') as f:
    resource_template = Template(f.read())

with open('templates/authenticator_tool_template.jinja2') as f:
    authenticator_template = Template(f.read())

# TODO update to new input files...
with open('input/github-fake.json') as f:
    input = json.load(f)

source_name = input['name']
source_name_capitalized = source_name.title()
source_type = input['type']

# Generate the authenticator tool
class_name = 'Bruinen' + source_name_capitalized + 'Authenticator'
tool_name = source_name_capitalized + ' Authenticator'

data = {
    'source_name': source_name,
    'class_name': class_name,
    'tool_name': tool_name
}

result = authenticator_template.render(data)
with open(f'bruinen_sdk/langchain_tools/{source_name}_authenticator_tool.py', 'w') as f:
    f.write(result)

# Generate the resource tools
for resource in input['resources']:
    resource_name = resource['name']
    resource_type = resource['type']

    class_name = 'Bruinen' + source_name.title() + resource_type.title() + resource_name.title() + 'Tool'
    tool_name = source_name.title() + ' ' + resource_type.title() + ' ' + resource_name.title()
    schema_name = source_name.title() + resource_type.title() + resource_name.title() + 'QuerySchema'
    
    # TODO pull this from JSON
    tool_description = 'Gets a list of Github repos for a user.'

    data = {
        'source_name': source_name,
        'class_name': class_name,
        'tool_name': tool_name,
        'tool_description': tool_description,
        'schema_name': schema_name,
        'parameters': [],
        'has_parameters': False
    }

    # TODO Mapping of JSON types to Python types
    # TODO look at Pydantic for this — we may be able to use this to flip it over automatically
    # null     > None
    # boolean  > bool
    # number   > int or float
    # string   > str
    # array    > list
    # object   > dict
    # date     > datetime.date
    # time     > datetime.time
    # datetime > datetime.datetime

    # Things to figure out
    #   How to handle dates
    #   How to handle number to int/float conversion

    # type_mapping = {
    #     "string": str,
    #     "number": Union[float, int],
    #     "integer": int,
    #     "boolean": bool,
    #     "array": List,
    #     "object": Dict
    # }
    def json_to_python_mapping(data):
        if data == 'null':
            return 'None'
        elif data == 'boolean':
            return 'bool'
        elif data == 'number':
            return 'int'
        elif data == 'string':
            return 'str'
        elif data == 'array':
            return 'list'
        elif data == 'object':
            return 'dict'
        elif data == 'date':
            return 'datetime.date'
        elif data == 'time':
            return 'datetime.time'
        elif data == 'datetime':
            return 'datetime.datetime'
        else:
            raise Exception('Unsupported JSON type')

    input_schema = resource['JSONInputSchema']

    # TODO we will need to add some sort of nested input types
    # TODO maybe not for input, but at least for output
    # TODO add output schema
    # TODO create example file that shows how to use the tools
    # TODO should take the input and output schemas, and parse the output into the Pydantic schema
    if 'properties' in input_schema.keys():
        data['has_parameters'] = True
        input_params = resource['JSONInputSchema']['properties']
        for param in input_params.keys():
            data['parameters'].append({
                'name': param,
                'type': json_to_python_mapping(input_params[param]['type']),
                'description': input_params[param]['description']
            })

    result = resource_template.render(data)
    with open(f'bruinen_sdk/langchain_tools/{source_name}_{resource_type}_{resource_name}_tool.py', 'w') as f:
        f.write(result)
