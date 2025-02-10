import boto3

def create_Ec2_instance():
    try:
        print("Creating Ec2 Instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId = "ami-abchdjeksjyuiokels",
            MinCount = 1,
            MaxCount = 1,
            InstanceType = "t2.micro",
            KeyName = "key pair name from aws console"
        )
        print("Created Ec2 Instance")
    except Exception as e:
        print(e)

create_Ec2_instance()