######################################################################################
# Dale Murdock 
# 2025-03-11
#
# List all routing profiles and arn in the instance
###################################################################################### 
 
import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv() # This loads the variables from the .env file

client = boto3.client('connect')

response = client.list_contact_flow_modules(
    InstanceId= os.getenv("INSTANCE_ID_OKTA"),
    #NextToken='string',
    MaxResults=200,
    ContactFlowModuleState='ACTIVE' #|'ARCHIVED'
)

cfms_list = response['ContactFlowModulesSummaryList']

# print(cfms_list)

module_ids = [item['Id'] for item in cfms_list]
# module_names = [item['Name'] for item in cfms_list]

# print(type(module_ids))

for i in module_ids:
    print(i)

# print(response)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)