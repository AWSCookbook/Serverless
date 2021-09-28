# Packaging Libraries with Lambda Layers


## Clean up 
### Delete the Lambda function:

`aws lambda delete-function --function-name AWSCookbook502Lambda`

### Delete the Lambda CloudWatch log group that was created automatically:
```
aws logs delete-log-group \
--log-group-name /aws/lambda/AWSCookbook502Lambda
```

### Delete the Lambda Layer:
```
aws lambda delete-layer-version \
    --layer-name AWSCookbook502RequestsLayer \
    --version-number 1
 ```

### Unset the environment variable that you created manually:
```
unset LAYER_VERSION_ARN
unset LAMBDA_ARN
```
