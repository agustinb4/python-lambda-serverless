import json
import boto3

# client for sqs
sqs_client = boto3.client('sqs', region_name='us-east-1')

def process(event, context):
    # Read param from request
    entity_id = event.get('queryStringParameters', {}).get('entityId')
    
    # Get queue info
    queue_url_info = sqs_client.get_queue_url(QueueName='dev-my-sqs')
    
    # Send message to sqs    
    sqs_client.send_message(QueueUrl=queue_url_info.get('QueueUrl'), 
                      MessageBody=entity_id)

    body = {
        "message": "Message sent to SQS",
        "input": event,
    }

    response = {
        "statusCode": 200, 
        "body": json.dumps(body)
    }

    return response
