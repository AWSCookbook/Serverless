#!/usr/bin/env python3

from aws_cdk import core

from cdk_aws_cookbook_512.cdk_aws_cookbook_512_stack import CdkAwsCookbook512Stack


app = core.App()
CdkAwsCookbook512Stack(app, "cdk-aws-cookbook-512")

app.synth()
