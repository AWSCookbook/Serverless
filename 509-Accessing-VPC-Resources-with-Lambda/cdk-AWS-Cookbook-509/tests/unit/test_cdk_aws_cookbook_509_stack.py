import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_aws_cookbook_509.cdk_aws_cookbook_509_stack import CdkAwsCookbook509Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_aws_cookbook_509/cdk_aws_cookbook_509_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkAwsCookbook509Stack(app, "cdk-aws-cookbook-509")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
