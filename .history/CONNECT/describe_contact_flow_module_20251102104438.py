import json
import os
import boto3
from dotenv import load_dotenv

load_dotenv() # This loads the variables from the .env file

list_cfm = ["list of contact flow module ids",
"list continues"]

client = boto3.client('connect')

for i in list:
    response = client.describe_contact_flow_module(
    InstanceId=os.getenv("INSTANCE_ID"),
    ContactFlowModuleId= i
    )

    # convert dict to json
    response_json = json.dumps(
        response,
        indent=4,
        sort_keys=True,
        default=str
    ) 
    i += ".json"

    with open(i, 'w') as json_file:
        json_file.write(response_json)