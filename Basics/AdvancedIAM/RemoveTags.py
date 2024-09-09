import boto3

iam_client = boto3.client('iam')

user_name='testupdated'

tags_keys = ['Department', 'Project']

iam_client.untag_user(UserName=user_name, TagKeys=tags_keys)
