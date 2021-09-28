# Triggering Lambda Functions on a Schedule
## Preparation
In the root of this Chapter’s repo cd to the “503-Triggering-Lambda-Functions-on-a-Schedule” directory and follow the subsequent steps: 

### Zip up the lambda_function.py provided in the repository:

`zip lambda_function.zip lambda_function.py`

### Create a Lambda function that we will trigger:
```
LAMBDA_ARN=$(aws lambda create-function \
--function-name AWSCookbook503Lambda \
--runtime python3.8 \
--package-type "Zip" \
--zip-file fileb://lambda_function.zip \
--handler lambda_function.lambda_handler --publish \
--role \
arn:aws:iam::$AWS_ACCOUNT_ID:role/AWSCookbookLambdaRole \
--output text --query FunctionArn)
```


## Clean up 
### Remove the target from the rule:
```
aws events remove-targets --rule "EveryMinuteEvent" \
--ids "1"
```

### Delete the rule:

`aws events delete-rule --name "EveryMinuteEvent"`

### Delete the Lambda function:

`aws lambda delete-function --function-name AWSCookbook503Lambda`

### Delete the Lambda CloudWatch log group:
```
aws logs delete-log-group \
--log-group-name /aws/lambda/AWSCookbook503Lambda
```

### Unset the environment variable that you created manually: 
```
unset LAMBDA_ARN
unset RULE_ARN
```
