# Automating CSV Import into DynamoDB from S3 with Lambda

## Clean up 
### Delete the DynamoDB table:
```
aws dynamodb delete-table \
--table-name 'AWSCookbook507'
```

### Delete the Lambda function:

`aws lambda delete-function --function-name AWSCookbook507Lambda`

### Delete the Lambda CloudWatch log group:
```
aws logs delete-log-group \
--log-group-name /aws/lambda/AWSCookbook507Lambda
```

### Detach the AmazonS3ReadOnlyAccess from the role:
```
aws iam detach-role-policy --role-name AWSCookbook507Lambda \
--policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

### Detach the AmazonDynamoDBFullAccess policy from the role:
```
aws iam detach-role-policy --role-name AWSCookbook507Lambda \
--policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess
```

### Detach the AWSLambdaBasicExecutionRole policy from the role:
```
aws iam detach-role-policy --role-name AWSCookbook507Lambda \
--policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

### Delete the IAM Role:

`aws iam delete-role --role-name AWSCookbook507Lambda`

### Delete the file you copied to your S3 bucket:

`aws s3 rm s3://awscookbook507-$RANDOM_STRING/sample_data.csv`

### Delete the S3 bucket:

`aws s3api delete-bucket --bucket awscookbook507-$RANDOM_STRING`

### Unset the environment variable that you created manually :
```
unset LAMBDA_ARN
unset RANDOM_STRING
```
