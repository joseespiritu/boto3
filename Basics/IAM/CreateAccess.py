import boto3

'''
def create_access(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)

create_access('testupdated')
'''

def update_access():
    iam = boto3.client('iam')

    iam.update_access_key(
        AccessKeyId='AKIAXLRU5M4V42HSVB27',
        Status='Inactive',
        UserName='testupdated'
    )

update_access()
