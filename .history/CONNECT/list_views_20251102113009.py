######################################################################################
# Dale Murdock 
# 2025-09-18
#
# Listing Views from a Connect Instance
######################################################################################

import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID")

client = boto3.client('connect')

if instance_id != "":
    response = client.list_views(

    InstanceId=os.getenv("INSTANCE_ID")
    )

else:
    instance_id = input("Please enter instance: ")
    response = client.describe_view(
    InstanceId=instance_id
    )

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)
# End of script