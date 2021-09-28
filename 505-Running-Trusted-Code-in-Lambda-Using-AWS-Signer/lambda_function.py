from datetime import datetime


def lambda_handler(event, context):
    print('AWS Cookbook Function run at {}'.format(str(datetime.now())))
