#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_aws_cookbook_504.cdk_aws_cookbook_504_stack import CdkAwsCookbook504Stack


app = cdk.App()
CdkAwsCookbook504Stack(app, "cdk-aws-cookbook-504")

app.synth()
