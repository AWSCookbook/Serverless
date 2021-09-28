# Running Trusted Code in Lambda Using Code Signing
## Preparation
In the root of this Chapter’s repo cd to the “505-Running-Trusted-Code-in-Lambda-Using-AWS-Signer” directory and follow the subsequent steps: 

### Set a unique suffix to use for the S3 bucket name and signing profile:
```
RANDOM_STRING=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)
```

### Create a Destination S3 bucket to store the signed code:

`aws s3api create-bucket --bucket awscookbook505-dst-$RANDOM_STRING`

### Create a Source S3 Bucket to store the raw code:

`aws s3api create-bucket --bucket awscookbook505-src-$RANDOM_STRING`

### Enable Versioning for the Source S3 bucket (this is required by AWS Signer):
```
aws s3api put-bucket-versioning \
--bucket awscookbook505-src-$RANDOM_STRING \
--versioning-configuration Status=Enabled
```

### Copy the provided lambda_function.zip file that contains the source code to the Source S3 bucket:

`aws s3 cp ./lambda_function.zip s3://awscookbook505-src-$RANDOM_STRING`

## Clean up 
### Delete the Lambda function:

`aws lambda delete-function --function-name AWSCookbook505Lambda`

### Delete the Lambda CloudWatch log group. This may not exist if you didn’t execute your Lambda function:
```
aws logs delete-log-group \
--log-group-name /aws/lambda/AWSCookbook505Lambda
```

### Revoke the signature:
```
aws signer revoke-signature --job-id $SIGNING_JOB_ID \
--reason "No longer using"
```

### Delete the code signing config:
```
aws lambda delete-code-signing-config \
--code-signing-config-arn $CODE_SIGNING_CONFIG_ARN
```

### Delete the signing profile:
```
aws signer cancel-signing-profile \
--profile-name AWSCookbook505_$RANDOM_STRING
```

### Delete all versions of files in the source S3 bucket:
```
aws s3api delete-objects \
    --bucket awscookbook505-src-$RANDOM_STRING \
    --delete "$(aws s3api list-object-versions \
    --bucket "awscookbook505-src-$RANDOM_STRING" \
    --output=json \
    --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')"
```

### Delete the source S3 bucket 

`aws s3api delete-bucket --bucket awscookbook505-src-$RANDOM_STRING`

### Delete the signed code in the destination bucket

`aws s3 rm s3://awscookbook505-dst-$RANDOM_STRING/$OBJECT_KEY`

### Delete the destination S3 bucket 

`aws s3api delete-bucket --bucket awscookbook505-dst-$RANDOM_STRING`

### Unset the environment variable that you created manually:
```
unset RANDOM_STRING
unset SIGNING_PROFILE_ARN
unset CODE_SIGNING_CONFIG_ARN
unset OBJ_VER_ID
unset SIGNING_JOB_ID
unset LAMBDA_ARN
unset OBJECT_KEY
```
