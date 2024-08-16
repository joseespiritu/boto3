import boto3

iam = boto3.client('iam')

response = iam.detach_user_policy(
    UserName='testuser2',
    PolicyArn='arn:aws:iam::aws:policy/AmazonRDSFullAccess'
)

print(response)