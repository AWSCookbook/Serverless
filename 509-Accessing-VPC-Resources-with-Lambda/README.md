# Accessing VPC Resources with Lambda
## Preparation

This recipe requires some “prep work” which deploys resources that you’ll build the solution on. You will use the AWS CDK to deploy these resources 

### In the root of this Chapter’s repo cd to the “509-Accessing-VPC-Resources-with-Lambda/cdk-AWS-Cookbook-509” directory and follow the subsequent steps:
```
cd 509-Accessing-VPC-Resources-with-Lambda/cdk-AWS-Cookbook-509
test -d .venv || python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cdk deploy
```

### Wait for the cdk deploy command to complete. 

### We created a helper.py script to let you easily create and export environment variables to make subsequent commands easier. Run the script, and copy the output to your terminal to export variables:

`python helper.py`

### For this recipe, you will need to create a modified environment variable from the output: 

`TRIMMED_ISOLATED_SUBNETS=$(echo ${ISOLATED_SUBNETS} | tr -d ' "')`

### We also need modify this variable to have the right format
`ISOLATED_SUBNETS=$(echo ${ISOLATED_SUBNETS} | tr -d ',"')`

### Go up a directory. 
```
cd ..
```

## Clean up 
### Delete the Cache Cluster:
```
aws elasticache delete-cache-cluster \
    --cache-cluster-id "AWSCookbook509CacheCluster"
```

### Delete the Cache Subnet Group:
```
aws elasticache delete-cache-subnet-group \
    --cache-subnet-group-name "AWSCookbook509CacheSG"
```

### Delete the Lambda function:

`aws lambda delete-function --function-name AWSCookbook509Lambda`

### Delete the Lambda CloudWatch log group:
```
aws logs delete-log-group \
--log-group-name /aws/lambda/AWSCookbook509Lambda
```

### Detach the AWSLambdaBasicExecutionRole policy from the role:
```
aws iam detach-role-policy --role-name AWSCookbook509Lambda \
--policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

### Delete the IAM Role:

`aws iam delete-role --role-name AWSCookbook509Lambda`

### Delete the Lambda Security Group: 

`aws ec2 delete-security-group --group-id $LAMBDA_SG_ID`

### To clean up the environment variables, run the helper.py script in this recipe’s cdk- directory with the --unset flag, and copy the output to your terminal to export variables:

`python helper.py --unset`

### Unset the environment variable that you created manually:
```
unset LAMBDA_SG_ID
unset LAMBDA_ARN
unset SUBNET_IDS
unset TRIMMED_ISOLATED_SUBNETS
```

### Use the AWS CDK to destroy the resources, deactivate your Python virtual environment, and go to the root of the chapter:

`cdk destroy && deactivate && rm -r .venv/ && cd ../..`
