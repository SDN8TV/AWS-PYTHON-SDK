import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv() # This loads the variables from the .env file

instance_id = os.getenv("CONNECT_INSTANCE_ID")
contact_flow_id = os.getenv("CONNECT_CONTACT_FLOW_ID")

client = boto3.client('connect')

response = client.describe_contact_flow(
    InstanceId= instance_id,
    ContactFlowId= contact_flow_id
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)