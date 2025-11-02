import json
import os
import boto3
from dotenv import load_dotenv

load_dotenv() # This loads the variables from the .env file

client = boto3.client('connect')

response = client.describe_contact_flow_module(
    InstanceId=os.getenv("INSTANCE_ID"),
    ContactFlowModuleId=os.getenv("CONTACT_FLOW_MODULE_ID")'
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)