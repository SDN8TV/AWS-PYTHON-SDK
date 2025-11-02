######################################################################################
# Dale Murdock 
# 2025-03-11
#
# List all routing profiles and arn in the instance
###################################################################################### 

import json
import boto3
import os
from dotenv import load_dotenv 
load_dotenv() # This loads the variables from the .env file

instance_id= os.getenv("CONNECT_INSTANCE_ID"),

connect = boto3.client('connect') #Connect
response = connect.list_routing_profiles(
    InstanceId= instance_id,
    MaxResults=250 # max results needs to account for the total number of routing profiles in the instance.
)

rp_list = response['RoutingProfileSummaryList'] # creates a  list from the dict

total_rp = 0

for arn in rp_list:
    length = len(arn['Arn'])
    arn_pure = (arn['Arn'])[length - 36:]
    print(arn['Name'], arn_pure)
    total_rp += 1
    #print(arn['Arn'])

print('\nTotal queues ', total_rp)
