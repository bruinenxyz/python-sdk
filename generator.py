from jinja2 import Template
import requests
from openapi_python_client.utils import snake_case

with open('templates/source_template.jinja2') as f:
    source_template = Template(f.read())

# Switch to production host when ready
host = 'http://localhost:3000'

response = requests.get(host + '/api-json')
if response.status_code == 200:
    json_data = response.json()

# TODO switch to pulling this from the OpenAPI schema
sources = ['github', 'google']

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
            if resource_name == 'callback':
                continue

            # GET, POST, etc.
            resource_methods = json_data['paths'][path].keys()
            for resource_method in resource_methods:
                # Get the parameters
                parameters = json_data['paths'][path][resource_method]['parameters']
                resource_parameters = []
                has_parameters = False
                for parameter in parameters:
                    if parameter['name'] != 'accountId':
                        has_parameters = True

                        # TODO find if Pydantic has an automatic way to do this, may need to make more flexible
                        def get_pydantic_type(json_type): 
                            if json_type == 'boolean':
                                return 'bool'
                            elif json_type == 'number':
                                return 'int'
                            elif json_type == 'string':
                                return 'str'                    
                            else:
                                raise Exception(f'Unsupported JSON type')

                        resource_parameters.append({
                            'name': parameter['name'],
                            'snake_case_name': snake_case(parameter['name']),
                            'required': parameter['required'],
                            'description': parameter['description'],
                            'type': parameter['schema']['type'],
                            'python_type': get_pydantic_type(parameter['schema']['type'])
                        })
                
                # TODO may need to change this as it's pretty brittle
                output_model = json_data['paths'][path][resource_method]['responses']['200']['content']['application/json']['schema']
                
                if output_model['type'] == 'array':
                    output_model_name = output_model['items']['title']
                    is_array = True
                else:
                    output_model_name = output_model['title']
                    is_array = False
                
                # TODO description could be changed to pull from somewhere
                resource_description = "Useful for when you need to " + resource_method + " a user's " + source_name.title() + " " + resource_name + "." 

                data['resources'].append({
                    'name': resource_name,
                    'type': resource_method,
                    'has_parameters': has_parameters,
                    'parameters': resource_parameters,
                    'class_name': source_name.title() + resource_method.title() + resource_name.title() + 'Tool',
                    'tool_name': source_name.title() + ' ' + resource_method.title() + ' ' + resource_name.title() + ' Tool',
                    'tool_description': resource_description,
                    'output_model_name': output_model_name,
                    'is_array': is_array,
                    'controller_name': source_name + '_controller_' + resource_name,
                })
    
    result = source_template.render(data)
    with open(f'bruinen/src/bruinen/langchain/{source_name}.py', 'w') as f:
        f.write(result)