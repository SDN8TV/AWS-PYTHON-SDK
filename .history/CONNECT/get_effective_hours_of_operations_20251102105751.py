import json
import os
import boto3
from dotenv import load_dotenv

load_dotenv() # This loads the variables from the .env file

client = boto3.client('connect')

response = client.get_effective_hours_of_operations(
    InstanceId='',
    HoursOfOperationId=os.getenv("HOO_ID_DEV"),
    FromDate='string',
    ToDate='string'
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)
#End of script