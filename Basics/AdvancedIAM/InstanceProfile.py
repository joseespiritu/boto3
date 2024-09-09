import boto3

iam = boto3.client('iam')

instance_profile_name = "MyNewEC2Profile"

iam.create_instance_profile(
    InstanceProfileName=instance_profile_name
)

print(f"Instance profile created {instance_profile_name}")