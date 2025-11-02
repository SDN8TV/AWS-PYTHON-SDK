######################################################################################
# Dale Murdock 
# 2025-09-18
#
# Describe a routing profile
######################################################################################

import json
import os
import boto3
from dotenv import load_dotenv

load_dotenv() # This loads the variables from the .env file

i_id=os.getenv("INSTANCE_ID")
rp_id=os.getenv("ROUTING_PROFILE_ID")

client = boto3.client('connect')

response = client.describe_routing_profile(
    InstanceId=i_id,
    RoutingProfileId=rp_id
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)

list_rp= ["list of routing profile ids",
"list continues"]

# for i in list_rp:
#     try:
#         client = boto3.client('connect')
#         response = client.describe_routing_profile(
#     InstanceId='string',
#     RoutingProfileId='string'
#     )
#     print(response)    
#     except:
#         pass

