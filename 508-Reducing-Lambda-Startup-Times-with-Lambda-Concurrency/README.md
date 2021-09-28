# Reducing Lambda Startup Times with Lambda Concurrency


## Clean up 
### Delete the Lambda function

`aws lambda delete-function --function-name AWSCookbook509Lambda`

### Delete the Lambda CloudWatch log group
```
aws logs delete-log-group \
--log-group-name /aws/lambda/AWSCookbook509Lambda
```
