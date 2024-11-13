# EC2 Management Automation

This project provides a set of Python scripts to manage EC2 instances on AWS using the `boto3` library. It allows you to list, launch, start, stop, and get details about EC2 instances. The code interacts with the AWS EC2 service using credentials and configuration stored in environment variables.

## Project Structure

```
C:\ALL_PROJECTS\puneWork\ec2Vm
│
├── .env                # AWS credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION)
├── .gitignore          # Git ignore file (ignores __pycache__)
├── automate_vm.py      # Script for automating EC2 instance tasks
├── check_vm_status.py  # Script to check the status of EC2 instances
├── create_vms.py       # Script to launch new EC2 instances
├── list_vms.py         # Script to list all EC2 instances
├── get_instance_info.py# Script to fetch details about a specific EC2 instance
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Prerequisites

Before running the scripts, ensure that you have:

- Python 3.x installed.
- AWS credentials (Access Key and Secret Key) with appropriate permissions to manage EC2 instances.
- The required Python libraries listed in `requirements.txt`.

You can install the dependencies with:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project directory with the following content:

```env
AWS_ACCESS_KEY_ID=<your-aws-access-key-id>
AWS_SECRET_ACCESS_KEY=<your-aws-secret-access-key>
AWS_REGION=<your-aws-region>
```

## Scripts

### 1. `list_vms.py`
This script lists all EC2 instances in the AWS account along with their current state (Running, Stopped, etc.) and instance type.

To run the script:

```bash
python list_vms.py
```

### 2. `create_vms.py`
This script launches a new EC2 instance with a specified name, instance type, and key pair.

To run the script:

```bash
python create_vms.py
```

You will be prompted to enter a name for the instance.

### 3. `get_instance_info.py`
This script retrieves detailed information about specific EC2 instances (e.g., instance state, type, CPU cores).

To run the script:

```bash
python get_instance_info.py
```

It will display available EC2 instances and prompt you to select one or show details for all instances.

### 4. `check_vm_status.py`
This script allows you to start, stop, or restart EC2 instances based on their instance ID.

To run the script and stop an instance:

```bash
python check_vm_status.py
```

You can modify the script to start or restart instances by changing the function call inside the script.

## How to Use

1. **Launch EC2 Instances**: Run `create_vms.py` to launch a new EC2 instance. You will be asked to provide the name of the instance.
   
2. **List All EC2 Instances**: Run `list_vms.py` to view all EC2 instances along with their status and type.

3. **Get EC2 Instance Information**: Run `get_instance_info.py` to view detailed information about specific instances. You can choose an instance by number or get information for all instances.

4. **Control EC2 Instances**: Use `check_vm_status.py` to start, stop, or restart EC2 instances by passing their instance ID.

## Example Output

### 1. `list_vms.py` output:

```
Instance ID: i-0dc8135ef1ab7869e, State: running, Instance Type: t2.micro
Instance ID: i-0bacc13de68a69674, State: stopped, Instance Type: t2.micro
```

### 2. `create_vms.py` output:

```
Enter the name for your EC2 instance: MyNewInstance
Instance i-0dc8135ef1ab7869e launched successfully!
```

### 3. `get_instance_info.py` output:

```
Available EC2 Instances:
1. Instance ID: i-0dc8135ef1ab7869e, Name: MyUbuntuInstance, State: running, Instance Type: t2.micro

Enter the number of the instance to get details, or enter 'all' to get details for all instances: 1

Instance ID: i-0dc8135ef1ab7869e
Instance State: running
Instance Type: t2.micro
CPU Cores Count: 1
'''EC2 instances do not directly provide CPU usage or memory usage.
CPU and Memory usage need to be monitored through CloudWatch metrics.'''
```

## Requirements

- **boto3**: The AWS SDK for Python to interact with AWS services.
- **python-dotenv**: For loading environment variables from the `.env` file.

You can install these dependencies with:

```bash
pip install -r requirements.txt
```



---

