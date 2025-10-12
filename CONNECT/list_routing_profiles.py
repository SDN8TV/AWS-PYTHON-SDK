import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file'

client = boto3.client('connect')

response = client.list_routing_profiles(
    InstanceId=os.getenv("INSTANCE_ID"),
    # NextToken='string',
    # MaxResults=123
)

rp_sum_list = response['RoutingProfileSummaryList']

for item in rp_sum_list:
    # print("Routing Profile Name :",item["Name"] + "\\t Routing Profile ID :", item["Id"])
    print(f"Routing Profile Name: {item['Name']} \033[12C Routing Profile ID: {item['Id']}")

