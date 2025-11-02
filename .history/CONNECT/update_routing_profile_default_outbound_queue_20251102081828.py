######################################################################################
# Dale Murdock 
# 2025-03-11
#
# Updates the default outbound queue of a routing profile.
######################################################################################

import boto3
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv() # This loads the variables from the .env file

client = boto3.client('connect')

response = client.update_routing_profile_default_outbound_queue(
    InstanceId= os.getenv("INSTANCE_ID_OKTA"),
    RoutingProfileId= os.getenv("ROUTING_PROFILE_ID_OKTA"),
    DefaultOutboundQueueId= os.getenv("QUEUE_ID_OKTA")
)