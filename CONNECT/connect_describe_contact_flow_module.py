import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv() # This loads the variables from the .env file


client = boto3.client('connect')

response = client.describe_contact_flow_module(
    InstanceId= os.getenv("INSTANCE_ID_OKTA"),
    ContactFlowModuleId=os.getenv("CONTACT_FLOW_MODULE_ID")
)

#print(type(response))
content = response['ContactFlowModule']['Content']

#content = json.loads(response['ContactFlowModule']['Content'])
print(type(content))
print(content)
find = "text key to look for in module content"

# Using the 'in' operator
if find in content:
    print(f"{find} found in text")

#module_ids = [item['Id'] for item in cfms_list]