import os
from datetime import datetime


def lambda_handler(event, context):
    print('AWS Cookbook Lambda function run at {}'.format(str(datetime.now())))
