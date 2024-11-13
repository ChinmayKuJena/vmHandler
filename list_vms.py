import boto3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_REGION')

# # Initialize EC2 client
# ec2_client = boto3.client('ec2', 
#                           aws_access_key_id=aws_access_key,
#                           aws_secret_access_key=aws_secret_key,
#                           region_name=region)

def list_all_instances_print():
    # Hardcoding the AWS credentials
    ec2_client = boto3.client('ec2', 
                          aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_key,
                          region_name=region)
    # Describe all EC2 instances
    response = ec2_client.describe_instances()

    # Iterate through the response to print instance details
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']  # Running, Stopped, etc.
            instance_type = instance['InstanceType']
            print(f"Instance ID: {instance_id}, State: {state}, Instance Type: {instance_type}")
def list_all_instances():
    """
    Retrieves and prints information about all EC2 instances in the AWS account.
    """
    ec2_client = boto3.client('ec2', 
                              aws_access_key_id=aws_access_key,
                              aws_secret_access_key=aws_secret_key,
                              region_name=region)
    
    # Describe all EC2 instances
    response = ec2_client.describe_instances()

    # Iterate through the response and print instance details
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']  # Running, Stopped, etc.
            instance_type = instance['InstanceType']
            name = 'N/A'
            # Try to get the 'Name' tag if it exists
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        name = tag['Value']
                        break
            instances.append((instance_id, state, instance_type, name))
    
    return instances

# List all EC2 instances
if __name__ == "__main__":
    # main()
    list_all_instances_print()
