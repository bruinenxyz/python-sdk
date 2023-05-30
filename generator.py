from jinja2 import Template
from typing import List, Dict, Union
import json, requests

# TODO change naming once it's updated
# TODO add description to JSON generated, e.g.
# tool_description = 'Get a list of Github repos for a user'

with open('templates/source_template.jinja2') as f:
    source_template = Template(f.read())

# loop through sources that we're going to use, should update to pull automatically from OpenAPI spec

# Switch to production host when ready
host = 'http://localhost:3000'

response = requests.get(host + '/api-json')
if response.status_code == 200:
    json_data = response.json()

# TODO switch to pulling this from the OpenAPI schema
sources = ['github']

for source in sources:
    data = {}

    # TODO update
    source_name = source
    # Create the authenticator tool
    authenticator_class_name = source_name.title() + 'AuthenticatorTool'
    authenticator_tool_name = source_name.title() + ' Authenticator Tool'

    data['source_name'] = source_name
    data['authenticator_class_name'] = authenticator_class_name
    data['authenticator_tool_name'] = authenticator_tool_name
    data['resources'] = []

    for path in json_data['paths'].keys():
        prefix = f'/sources/{source_name}/'
        if path.startswith(prefix):
            resource_name = path[len(prefix):]
            # print(resource_name)
            if resource_name == 'callback':
                continue

            # GET, POST, etc.
            resource_methods = json_data['paths'][path].keys()
            for resource_method in resource_methods:
                # Get the parameters
                
                parameters = json_data['paths'][path][resource_method]['parameters']
                resource_parameters = []
                # TODO test if there are parameters
                has_parameters = False
                for parameter in parameters:
                    if parameter['name'] != 'accountId':
                        has_parameters = True
                        # TODO figure out how to deal with the schema
                        resource_parameters.append({
                            'name': parameter['name'],
                            'required': parameter['required'],
                            'description': parameter['description'],
                            'schema': parameter['schema'],
                        })
                
                # TODO may need to change this as it's pretty brittle
                output_model = json_data['paths'][path][resource_method]['responses']['200']['content']['application/json']['schema']
                
                if output_model['type'] == 'array':
                    output_model_name = output_model['items']['title']
                    is_array = True
                else:
                    output_model_name = output_model['title']
                    is_array = False
                

                
                # print(resource_name)
                # print(output_model['type'])
                # print()
                # output_model_name = json_data['paths'][path][resource_method]['responses']['200']['content']['application/json']['schema']['title']
                # Figure out if output is a single object or a list
                # print(resource_name)
                # print(json_data['paths'][path][resource_method]['responses']['200'])
                # print('')
                
                # TODO description could be changed to pull from somewhere
                resource_description = "Useful for when you need to " + resource_method + " a user's " + source_name.title() + " " + resource_name + "." 

                data['resources'].append({
                    'name': resource_name,
                    'type': resource_method,
                    'has_parameters': has_parameters,
                    'parameters': parameters,
                    'class_name': source_name.title() + resource_method.title() + resource_name.title() + 'Tool',
                    'tool_name': source_name.title() + ' ' + resource_method.title() + ' ' + resource_name.title() + ' Tool',
                    'tool_description': resource_description,
                    'output_model_name': output_model_name,
                    'is_array': is_array,
                    'controller_name': source_name + '_controller_' + resource_name,
                })
            


    # print(data)
    # exit()
    

    result = source_template.render(data)
    with open(f'bruinen/src/bruinen/langchain/{source_name}.py', 'w') as f:
        f.write(result)







exit()

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
