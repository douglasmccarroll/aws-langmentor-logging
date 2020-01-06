import json
import os
import boto3

print('Loading LangMentorLogMessage function...')

def lambda_handler(input, context):
    body = input["body"]
    jsonBody = json.loads(body)
    subject = jsonBody["subject"]
    message = jsonBody["message"]
    sns = boto3.client('sns')
    sns.publish(
        TopicArn=os.environ.get('SNS_TOPIC_ARN'),
        Subject=subject,
        Message=message
    )
    return {
        'statusCode': 200
    }