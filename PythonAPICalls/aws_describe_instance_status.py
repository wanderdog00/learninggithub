import boto3
import json

ec2 = boto3.client('ec2')

response = ec2.describe_instance_status(Filters=[{'Name' : 'event.code','Values' : ['instance-reboot','system-reboot','system-maintenance','instance-retirement','instance-stop']}])

print(response)

