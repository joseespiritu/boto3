import json
from datetime import datetime

import boto3

iam = boto3.client('iam')

current_date = datetime.now().strftime('%Y-%m-%d')

start_time=f"{current_date}T01:00:00Z"
end_time=f"{current_date}T03:00:00Z"

policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::demo-cloudfront-jlme-v4/*",
            "Condition": {
                "DateGreaterThan": {"aws:CurrentTime": start_time},
                "DateLessThan": {"aws:CurrentTime": end_time}
            }
        }
    ]
}

try:
    response = iam.create_policy(
        PolicyName='AccessWindowPolicyNew',
        PolicyDocument=json.dumps(policy_document)
    )

    print(f"IAM conditional created")
except Exception as e:
    print(e)