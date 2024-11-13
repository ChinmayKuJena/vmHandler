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
def launch_instance():
    instance_name = input("Enter the name for your EC2 instance: ")
    
    ec2_client = boto3.client('ec2', 
                          aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_key,
                          region_name=region)

    # Launch an EC2 instance with a specific AMI, instance type, and key pair
    response = ec2_client.run_instances(
        ImageId='ami-0dee22c13ea7a9a67',  # Ubuntu AMI ID
        InstanceType='t2.micro',  # Change if you need a different instance type
        MinCount=1,
        MaxCount=1,
        KeyName='test',  # Replace with your actual key pair name
        SecurityGroupIds=['sg-056b2507b13e93c1c'],  # Replace with your security group ID (default works)
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{
                'Key': 'Name',
                'Value': instance_name
            }]
        }]
    )

    # Get the instance details from the response
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance {instance_id} launched successfully!")

# Call the function to launch the instance
launch_instance()
