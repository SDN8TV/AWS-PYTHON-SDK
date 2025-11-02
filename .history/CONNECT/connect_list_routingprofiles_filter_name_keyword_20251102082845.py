######################################################################################
# Dale Murdock 
# 2025-03-11
#
# List routing profiles and arn, filter by keyword in the name of the routing profile
######################################################################################

import json
import boto3
import os
from dotenv import find_dotenv, load_dotenv 
load_dotenv() # This loads the variables from the .env file

keyword = 'Chat'
instance_id= os.getenv("CONNECT_INSTANCE_ID")

connect = boto3.client('connect') #Connect
response = connect.list_routing_profiles(
    InstanceId= instance_id,
    MaxResults=250 # max results needs to account for the total number of routing profiles in the instance.
)

rp_list = response['RoutingProfileSummaryList'] # creates a  list from the dict

total_rp = 0

for arn in rp_list:
    if keyword in arn['Name']:
        length = len(arn['Arn'])
        arn_pure = (arn['Arn'])[length - 36:]
        #print(arn['Name'], arn_pure)
        print(arn_pure)
        total_rp += 1
    else:
        pass

print('\nTotal Routing Profiles ', total_rp)
