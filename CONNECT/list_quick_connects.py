import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

client = boto3.client('connect')

response = client.list_quick_connects(
    InstanceId=os.getenv("INSTANCE_ID"),
    # NextToken='string',
    MaxResults=100,
    QuickConnectTypes=[
        'QUEUE'
    ]
)

print(response)

#response from aws is a dict
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) #convert dict to json

print(response_json)