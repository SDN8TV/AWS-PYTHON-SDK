######################################################################################
# Dale Murdock 
# 2025-09-19
#
# This will describe the hour of operations overrides
######################################################################################

import json
import os
import boto3
from dotenv import load_dotenv

load_dotenv() # This loads the variables from the .env file

instance_id =os.getenv("INSTANCE_ID_SANDBOX")
hoo_id =os.getenv("HOO_ID_SANDBOX")
hoo_o_id=os.getenv("HOO_OVERRIDE_ID_SANDBOX")   

client = boto3.client('connect')

response = client.describe_hours_of_operation_override(
    InstanceId=instance_id,
    HoursOfOperationId=hoo_id,
    HoursOfOperationOverrideId=hoo_o_id
)

# convert dict to json
response_json = json.dumps(
   response,
   indent=4,
   sort_keys=True,
   default=str
)

print(response_json)
# End of script