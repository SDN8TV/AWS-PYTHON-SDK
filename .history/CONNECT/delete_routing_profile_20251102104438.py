import json
import os
import boto3
from dotenv import load_dotenv

load_dotenv() # This loads the variables from the .env file

client = boto3.client('connect')

response = client.delete_routing_profile(
    InstanceId=os.getenv("INSTANCE_ID"),
    RoutingProfileId=os.getenv("ROUTING_PROFILE_ID")
)
    
# convert dict to json
response_json = json.dumps(
    response,
    indent=4,
    sort_keys=True,
    default=str
)
    
print(response_json)
    


    










client = boto3.client('connect')

response = client.delete_routing_profile(
    InstanceId='string',
    RoutingProfileId='string'
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)