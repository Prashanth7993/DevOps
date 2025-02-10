import boto3

def create_Ec2_instance():
    try:
        print("Creating Ec2 Instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId = "ami-085ad6ae776d8f09c",
            MinCount = 1,
            MaxCount = 1,
            InstanceType = "t2.micro",
            KeyName = "AdminN-Virginia"
        )
        print("Created Ec2 Instance")
    except Exception as e:
        print(e)

create_Ec2_instance()