# get_instance_info.py
import boto3
from dotenv import load_dotenv
import os
from list_vms import list_all_instances

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_REGION')

# Initialize EC2 client
ec2_client = boto3.client('ec2', 
                          aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_key,
                          region_name=region)


def get_instance_info(instance_id):
    """
    Retrieves and prints information about a specific EC2 instance.
    """
    try:
        # Describe the EC2 instance
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        
        # Extract instance information
        instance_info = response['Reservations'][0]['Instances'][0]
        
        instance_state = instance_info['State']['Name']  # State of the instance
        instance_type = instance_info['InstanceType']  # Instance type (e.g., t2.micro)
        
        # EC2 instances do not directly provide CPU usage or memory usage.
        # CPU and Memory usage need to be monitored through CloudWatch metrics.
        cpu_cores = instance_info.get('CpuOptions', {}).get('CoreCount', 'N/A')  # Get the CPU cores
        # memory = instance_info.get('MemoryInfo', {}).get('SizeInMiB', 'N/A')  # Memory in MiB
        
        # Print out information
        print(f"Instance ID: {instance_id}")
        print(f"Instance State: {instance_state}")
        print(f"Instance Type: {instance_type}")
        print("'''EC2 instances do not directly provide CPU usage or memory usage.\nCPU and Memory usage need to be monitored through CloudWatch metrics.''' ")
        print(f"CPU Cores Count: {cpu_cores}")
        # print(f"Memory: {memory} MiB")

    except Exception as e:
        print(f"Error retrieving instance information: {e}")


def main():
    # Fetch the list of EC2 instances using the list_all_instances function from list_instances.py
    instances = list_all_instances()

    if not instances:
        print("No EC2 instances found.")
        return

    # Display available instances to the user
    print("Available EC2 Instances:")
    for index, (instance_id, state, instance_type, name) in enumerate(instances, start=1):
        print(f"{index}. Instance ID: {instance_id}, Name: {name}, State: {state}, Instance Type: {instance_type}")

    # Ask the user to select an instance or choose 'all' to get details of all instances
    user_input = input("\nEnter the number of the instance to get details, or enter 'all' to get details for all instances: ")

    if user_input.lower() == 'all':
        # Show details for all instances
        for instance_id, _, _, _ in instances:
            get_instance_info(instance_id)
    else:
        try:
            selected_index = int(user_input) - 1
            if 0 <= selected_index < len(instances):
                selected_instance_id = instances[selected_index][0]
                get_instance_info(selected_instance_id)
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'all'.")


# Run the main function
if __name__ == "__main__":
    main()
