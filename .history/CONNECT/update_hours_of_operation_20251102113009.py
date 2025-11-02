######################################################################################
# Dale Murdock 
# 2025-04-09
#
# 
###################################################################################### 

import json
import boto3

client = boto3.client('connect')

response = client.update_hours_of_operation(
    InstanceId='string',
    HoursOfOperationId='string',
    Name='string',
    Description='string',
    TimeZone='string',
    Config=[
        {
            'Day': 'SUNDAY'|'MONDAY'|'TUESDAY'|'WEDNESDAY'|'THURSDAY'|'FRIDAY'|'SATURDAY',
            'StartTime': {
                'Hours': 123,
                'Minutes': 123
            },
            'EndTime': {
                'Hours': 123,
                'Minutes': 123
            }
        },
    ]
)