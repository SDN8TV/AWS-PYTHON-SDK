######################################################################################
# Dale Murdock 
# 2025-04-09
#
######################################################################################  

import json
import os
import boto3
from dotenv import load_dotenv 
load_dotenv() # This loads the variables from the .env file

instance_id = os.getenv("CONNECT_INSTANCE_ID")
queue_name = os.getenv("QUEUE_NAME")
tz = os.getenv("TZ")
hoo_id = os.getenv("HOO_ID")

client = boto3.client('connect')

response = client.create_queue(
    InstanceId= instance_id,
    Name= queue_name,
    Description= queue_name,
    # OutboundCallerConfig={
    #     'OutboundCallerIdName': 'string',
    #     'OutboundCallerIdNumberId': 'string',
    #     'OutboundFlowId': 'string'
    # },
    # OutboundEmailConfig={
    #     'OutboundEmailAddressId': 'string'
    # },
    HoursOfOperationId= hoo_id,
    # MaxContacts=123,
    # QuickConnectIds=[
    #     'string',
    # ],
    # Tags={
    #     'string': 'string'
    # }
)

#convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 ) 

print(response_json)