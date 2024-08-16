import boto3

def delete_user(username):
    iam = boto3.client('iam')

    response = iam.delete_user(
        UserName=username
    )

    print(response)

delete_user('testuser2')
