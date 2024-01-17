import json
import boto3

# client for sqs
sqs_client = boto3.client('sqs', region_name='us-east-1', endpoint_url='http://localhost:9324')


def process(event, context):
    # Read param from request
    entity_id = event.get('queryStringParameters', {}).get('entityId')
    print(f'Processing entity id {entity_id}')

    # Get queue info
    queue_url_info = sqs_client.get_queue_url(QueueName='local-my-sqs')

    # Send message to sqs
    sqs_client.send_message(QueueUrl=queue_url_info.get('QueueUrl'),
                            MessageBody=json.dumps({'entity_id': str(entity_id)}))

    body = {
        "message": "Message sent to SQS",
        "input": entity_id,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


if __name__ == "__main__":
    process({'queryStringParameters': {'entityId': 123456}}, None)
