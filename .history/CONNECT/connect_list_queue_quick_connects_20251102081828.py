import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv 
load_dotenv() # This loads the variables from the .env file



#list all groups using client
connect = boto3.client('connect') #Connect
response = connect.list_queue_quick_connects(
    InstanceId=os.getenv("CONNECT_INSTANCE_ID"),
    QueueId=os.getenv("CONNECT_QUEUE_ID")
)

qcsl_list = response['QuickConnectSummaryList'] #set variable equal to the QueueSummaryList list
#response from aws is a dict

#print(qcsl_list)

qcsl_names = [item['Name'] for item in qcsl_list] #creates a list of the quick connects assigned to the queue

#print(type(qcsl_names))
print("\n".join(qcsl_names))

# qcsl_list_json = json.dumps(
#     qcsl_list,
#     indent=4,
#     sort_keys=True,
#     default=str
# ) #convert dict to json

# print(qcsl_list_json)