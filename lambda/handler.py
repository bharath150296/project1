import boto3
import uuid
import json
import os


dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

sns = boto3.client('sns')

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    user_id = str(uuid.uuid4())
    message = event.get('message', 'Hello, World!')
    table.put_item(
        Item={
            'UserId': user_id,
            'Message': message
        }
    )
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message='Lambda executed successfully'
        )
    return {
        'statusCode': 200,
        'body': json.dumps({
            'UserId': user_id,
            'Message': message
        })
    }