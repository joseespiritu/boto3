import boto3

ses_client = boto3.client('ses')

resp = ses_client.send_templated_email(
    Source='email@gmail.com',
    Destination={
        'ToAddresses':['email@gmail.com'],
        'CcAddresses':['email@gmail.com']
    },
    ReplyToAddresses=['email@gmail.com'],
    Template='CustomTemplate',
    TemplateData='{"replace":"value"}'
)

print(resp)