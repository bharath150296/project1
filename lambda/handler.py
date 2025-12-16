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

    http_method = event.get('httpMethod')
    path = event.get('path')
    # if http_method == 'POST' and path == '/app':
    body = json.loads(event.get('body', '{}'))
    phone_number = body.get('phoneNumber')
    message = body.get('message', 'Default message from POST')
    if not phone_number:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'phoneNumber is required'})
        }
    table.put_item(
        Item={
            'id': phone_number,
            'Message': message
        }
    )
    user_id = str(uuid.uuid4())
    # message = event.get('message', 'Hello, World!')
    # table.put_item(
    #     Item={
    #         'id': user_id,
    #         'Message': message
    #     }
    # )
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