import json
import boto3

# client for S3
s3_client = boto3.client('s3', region_name='us-east-1', endpoint_url='http://localhost:4566')


def process(event, context):
    # Read messages from sqs in batch
    sqs_messages = event.get('Records')
    for message in sqs_messages:
        print("Reading message from SQS")
        body = message.get('body', {})
        body_json = json.loads(body)
        print(f'Message body: {body_json}')

        # Create file in s3
        s3_client.put_object(Body=body_json.get('entity_id'),
                             Bucket='my-bucket',
                             Key=body_json.get('entity_id'))

    print('All messages processed')

    response = {
        "statusCode": 200,
        "body": "OK"
    }

    return response
