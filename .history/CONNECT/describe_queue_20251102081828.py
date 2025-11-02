######################################################################################
# Dale Murdock 
# 2025-03-11
#
# describe queue
###################################################################################### 

import boto3
import json

i_id=''
q_id=''

client = boto3.client('connect')

response = client.describe_queue(
    InstanceId=i_id,
    QueueId=q_id
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)