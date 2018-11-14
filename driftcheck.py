import boto3
ec2client = boto3.client('ec2','us-east-1')

regions = ec2client.describe_regions(RegionNames=[ 'us-east-1' ] )
for region in regions["Regions"]:
   reg = region['RegionName']   
   stack_session = boto3.client('cloudformation',region['RegionName'])
   paginator = stack_session.get_paginator('list_stacks')
   response_iterator = paginator.paginate()
   for page in response_iterator:
       stacks = page['StackSummaries']
       for stack in stacks:
         print(stack['StackName'])
         try:
             response = stack_session.detect_stack_drift(StackName = stack['StackName'])
         except:
             print("Failed")