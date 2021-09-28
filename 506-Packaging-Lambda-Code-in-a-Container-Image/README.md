# Packaging Lambda Code in a Container Image
## Preparation
### Create an ECR repository to store your Docker image:

`aws ecr create-repository --repository-name aws-cookbook-506repo`



## Clean up 
### Delete the Lambda function:

`aws lambda delete-function --function-name AWSCookbook506Lambda`

### Delete the Lambda CloudWatch log group:
```
aws logs delete-log-group \
--log-group-name /aws/lambda/AWSCookbook506Lambda
```

### Delete the images from your local machine:
```
docker image rm lambda-cookbook-container:latest
docker image rm \
$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/aws-cookbook-506repo:latest
```

### Remove the image from ECR:
```
aws ecr batch-delete-image \
--repository-name aws-cookbook-506repo \
--image-ids imageTag=latest
```

### Delete the now empty repository:
```
aws ecr delete-repository \
--repository-name aws-cookbook-506repo
```

### Unset the environment variable that you created manually

`unset LAMBDA_ARN`
