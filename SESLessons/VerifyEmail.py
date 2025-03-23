import boto3

ses_client = boto3.client('ses')

response = ses_client.verify_email_address(
    EmailAddress='email@gmail.com'
)

print(response)