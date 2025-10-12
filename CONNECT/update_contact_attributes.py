import boto3
import json 

client = boto3.client('connect')

response = client.update_contact_attributes(
    InitialContactId='string',
    InstanceId='string',
    Attributes={
        'oncallNumber': '+18005551212'
    }
)

# convert dict to json
response_json = json.dumps(
     response,
     indent=4,
     sort_keys=True,
     default=str
 )

print (response_json)