import boto3

def sed_email_text():
    ses_client = boto3.client('ses')
    CHARSET='UTF-8'

    response = ses_client.send_email(
        Destination={
            "ToAddresses":[
                "email@gmail.com"
            ]
        },
        Message={
            "Body":{
                "Text":{
                    "Charset":CHARSET,
                    "Data":"Thanks for buying the course"
                }
            },
            "Subject":{
                "Charset":CHARSET,
                "Data":"AWS Course with Python & Boto3"
            }
        },
        Source = "email@gmail.com",
    )

    print(response)

sed_email_text()