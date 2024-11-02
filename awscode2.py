import boto3

ec2 = boto3.client('ec2', region_name="us-east-1")
#_iam = boto3.client('iam')
# _s3 = boto3.client('s3')

response = ec2.describe_instances()
for instance in response['Reservations']:
    print(instance['Instances'][0]['InstanceId'])