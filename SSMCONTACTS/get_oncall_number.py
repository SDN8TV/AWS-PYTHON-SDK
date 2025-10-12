import boto3
import json
import os
from dotenv import find_dotenv, load_dotenv 

load_dotenv() # This loads the variables from the .env file

rotation_name= os.getenv("ROTATION_NAME")
initialContactId= os.getenv("INITIAL_CONTACT_ID")       
instanceId= os.getenv("INSTANCE_ID")

### connecton clients 
ssmcontact_client = boto3.client('ssm-contacts')
connect_client = boto3.client('connect')

### functions
def get_contact_id(rotation_name, client):
    response = client.list_rotations(
    RotationNamePrefix= rotation_name
    )
    contact_id = str(response['Rotations'][0]['ContactIds'][0])
    contact_id = contact_id.strip("[']")
    print(contact_id)
    return contact_id

def get_oncall_number(contact_id, client):
    response = client.list_contact_channels(
    ContactId= contact_id
    )
    print(response['ContactChannels'][0]['DeliveryAddress']['SimpleAddress'])
    oncall_number = str(response['ContactChannels'][0]['DeliveryAddress']['SimpleAddress'])
    return oncall_number

def update_contact_attributes(oncall_number, contact_id, instance_id, client):
    response = client.update_contact_attributes(
    InitialContactId= contact_id,
    InstanceId= instance_id,
    Attributes={
        'oncallNumber': oncall_number
    }
    )
    return response


  
try:
    rotation_name= input("Enter Rotation Name :")
    initialContactId= input("Enter Contact ID :")
    instanceId= input("Enter Instance ID :")
    contact_id= get_contact_id(rotation_name, ssmcontact_client)
    oncall_number= get_oncall_number(contact_id, ssmcontact_client)
    response= update_contact_attributes(oncall_number, initialContactId, instanceId, connect_client)
    if response == {}:
        print("Contact Attributes Updated Successfully")
except Exception as e:
    print("Error: ", e)
    print("Please check the input parameters")
    


