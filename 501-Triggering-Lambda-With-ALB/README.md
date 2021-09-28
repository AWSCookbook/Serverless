# Triggering Lambda With ALB
## Preparation
This recipe requires some “prep work” which deploys resources that you’ll build the solution on. You will use the AWS CDK to deploy these resources.

### In the root of this Chapter’s repo cd to the “501-Triggering-Lambda-With-ALB/cdk-AWS-Cookbook-501” directory and follow the subsequent steps: 
```
cd 501-Triggering-Lambda-With-ALB/cdk-AWS-Cookbook-501/
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

`PUBLIC_SUBNETS=$(echo ${PUBLIC_SUBNETS} | tr -d ',"')`

### Navigate up to the main directory for this recipe (out of the “cdk-AWS-Cookbook-501” directory):

`cd ..`



## Clean up 
### Delete the listener rule:

`aws elbv2 delete-rule --rule-arn $RULE_ARN`

### Delete the target group:

`aws elbv2 delete-target-group --target-group-arn $TARGET_GROUP_ARN`

### Delete the Lambda function:

`aws lambda delete-function --function-name AWSCookbook501Lambda`

### Delete the Lambda CloudWatch log group:
```
aws logs delete-log-group \
--log-group-name /aws/lambda/AWSCookbook501Lambda
```

### Go to the cdk-AWS-Cookbook-501 directory:

`cd cdk-AWS-Cookbook-501/`

### To clean up the environment variables, run the helper.py script in this recipe’s cdk- directory with the --unset flag, and copy the output to your terminal to export variables:

`python helper.py --unset`

### Unset the environment variable that you created manually: 
```
unset LAMBDA_ARN
unset RULE_ARN
unset TARGET_GROUP_ARN
```

### Use the AWS CDK to destroy the resources, deactivate your Python virtual environment, and go to the root of the chapter:

`cdk destroy && deactivate && rm -r .venv/ && cd ../..`

