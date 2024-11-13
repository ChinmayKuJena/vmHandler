import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_REGION')
# Function to initialize the EC2 client
def initialize_ec2_client():
    ec2_client = boto3.client('ec2', 
                          aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_key,
                          region_name=region)
    return ec2_client

# Function to start an EC2 instance
def start_instance(instance_id):
    ec2_client = initialize_ec2_client()
    try:
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Starting instance: {instance_id}")
        print(response)
    except ClientError as e:
        print(f"Error starting instance {instance_id}: {e}")

# Function to stop an EC2 instance
def stop_instance(instance_id):
    ec2_client = initialize_ec2_client()
    try:
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance: {instance_id}")
        print(response)
    except ClientError as e:
        print(f"Error stopping instance {instance_id}: {e}")

# Function to restart (reboot) an EC2 instance
def restart_instance(instance_id):
    ec2_client = initialize_ec2_client()
    try:
        response = ec2_client.reboot_instances(InstanceIds=[instance_id])
        print(f"Restarting (rebooting) instance: {instance_id}")
        print(response)
    except ClientError as e:
        print(f"Error restarting instance {instance_id}: {e}")

# Example Usage
if __name__ == '__main__':
    instance_id = 'i-0dc8135ef1ab7869e'  # Replace with your EC2 instance ID
    
    # Start the instance
    # start_instance(instance_id)
    
    # Stop the instance
    stop_instance(instance_id)
    
    # Restart the instance
    # restart_instance(instance_id)
