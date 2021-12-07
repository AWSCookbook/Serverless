# Mounting an EFS Filesystem to Lambda Functions
## Preparation
This recipe requires some “prep work” which deploys resources that you’ll build the solution on. You will use the AWS CDK to deploy these resources 

### In the root of this Chapter’s repo cd to the “504-Mounting-an-EFS-Filesystem-to-Lambda/cdk-AWS-Cookbook-504” directory and follow the subsequent steps: 
```
cd 504-Mounting-an-EFS-Filesystem-to-Lambda/cdk-AWS-Cookbook-504/
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

`ISOLATED_SUBNETS=$(echo ${ISOLATED_SUBNETS} | tr -d ' "')`

### Navigate up to the main directory for this recipe (out of the “cdk-AWS-Cookbook-504” directory)

`cd ..`



## Clean up 
### Delete the Lambda function:

`aws lambda delete-function --function-name AWSCookbook504Lambda`

### Delete the Lambda CloudWatch log group:
```
aws logs delete-log-group \
--log-group-name /aws/lambda/AWSCookbook504Lambda
```

### Detach the LambdaVPCAccessExecutionPolicy from the role:
```
aws iam detach-role-policy --role-name AWSCookbook504Role \
--policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole
```
### Delete the IAM Role:

`aws iam delete-role --role-name AWSCookbook504Role`

### Remove the ingress rule to the EFS File System’s Security group that allows access on port tcp 2049 from the Lambda’s Security Group:
```
aws ec2 revoke-security-group-ingress \
--protocol tcp --port 2049 \
--source-group $LAMBDA_SG_ID \
--group-id $EFS_SECURITY_GROUP
```

### Delete the security group that you created for the Lambda function:

`aws ec2 delete-security-group --group-id $LAMBDA_SG_ID`

### Go to the cdk-AWS-Cookbook-504 directory:

`cd cdk-AWS-Cookbook-504/`

### To clean up the environment variables, run the helper.py script in this recipe’s cdk- directory with the --unset flag, and copy the output to your terminal to export variables:

`python helper.py --unset`

### Unset the environment variable that you created manually:
```
unset LAMBDA_ARN
unset LAMBDA_SG_ID
```

### Use the AWS CDK to destroy the resources, deactivate your Python virtual environment, and go to the root of the chapter:

`cdk destroy && deactivate && rm -r .venv/ && cd ../..`

