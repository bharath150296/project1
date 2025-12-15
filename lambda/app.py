import boto3
import uuid
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserMessages')
def lambda_handler(event, context):
    user_id = str(uuid.uuid4())
    message = event.get('message', 'Hello, World!')
    table.put_item(
        Item={
            'UserId': user_id,
            'Message': message
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps({
            'UserId': user_id,
            'Message': message
        })
    }