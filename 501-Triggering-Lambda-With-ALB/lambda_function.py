import json
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps('This AWSCookbook Lambda function was invoked from an Application Load Balancer!\n')
    }
