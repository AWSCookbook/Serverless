#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_aws_cookbook_501.cdk_aws_cookbook_501_stack import CdkAwsCookbook501Stack


app = cdk.App()
CdkAwsCookbook501Stack(app, "cdk-aws-cookbook-501")

app.synth()
