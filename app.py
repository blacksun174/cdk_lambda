#!/usr/bin/env python3

from aws_cdk import cdk

from cdk_lambda.cdk_lambda_stack import CdkLambdaStack


app = cdk.App()
CdkLambdaStack(app, "cdk-lambda-cdk-1")

app.run()
