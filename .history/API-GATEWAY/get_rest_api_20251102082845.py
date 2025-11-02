######################################################################################
# Dale Murdock 
# 
######################################################################################

import json
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

api_id =os.getenv("API_ID")

client = boto3.client('apigateway')

response = client.get_rest_api(
    restApiId=api_id
)

# convert dict to json
response_json = json.dumps(
   response,
   indent=4,
   sort_keys=True,
   default=str
)

print(response_json)

