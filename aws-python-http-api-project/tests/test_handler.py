import json
import unittest
from ..publisher import process


class TestHandler(unittest.TestCase):

    def test_handler_invocation(self):
        event = {
            'queryStringParameters': {
                'entityId': 12345
            }
        }

        # Run
        response = process(event, None)

        # Asserts
        self.assertEqual(response, {
            "statusCode": 200,
            "body": json.dumps({"message": "Message sent to SQS", "input": 12345})
        })


if __name__ == '__main__':
    unittest.main()
