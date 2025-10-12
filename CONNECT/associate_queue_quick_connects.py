import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv 
load_dotenv() # This loads the variables from the .env file 

quick_connect_id1 =os.getenv("CONNECT_QUICK_CONNECT_ID1")
quick_connect_id2 =os.getenv("CONNECT_QUICK_CONNECT_ID2")

client = boto3.client('connect')

response = client.associate_queue_quick_connects(
    InstanceId=os.getenv("CONNECT_INSTANCE_ID"),
    QueueId=os.getenv("CONNECT_QUEUE_ID"),
    QuickConnectIds=[
        quick_connect_id1,
        quick_connect_id2
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


