#!/usr/bin/env python3

from aws_cdk import cdk

from cdk_lambda.cdk_lambda_stack import CdkLambdaStack
from aws_cdk import \
    aws_events as events, \
    aws_lambda as lambda_, \
    cdk, aws_events_targets as targets, \
    aws_apigateway as apigateway


class LambdaCronStack(cdk.Stack):
    def __init__(self, app: cdk.App, id: str) -> None:
        super().__init__(app, id)

        with open("lambda-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()

        lambdaFn = lambda_.Function(
            self,
            id="commentableNewsRecommenderStg1",
            code=lambda_.InlineCode(handler_code),
            handler="index.lambda_handler",
            function_name='commentableNewsRecommenderStg1',
            timeout=300,
            runtime=lambda_.Runtime.PYTHON36,
        )

        api = apigateway.LambdaRestApi(self, handler=lambdaFn, id='commentableNewsRecommendersStg1')
        api.root.add_method(http_method='POST')
        # a = apigateway.RestApi(self, id='commentableNewsRecommenderStg1', rest_api_name='commentableNewsRecommenderStg1')



        # gateway = apigateway.LambdaRestApi(handler=lambdaFn)

        # Run every day at 6PM UTC
        # See https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html
        # rule = events.Rule(
        #     self, "Rule", schedule="cron(0 18 ? * MON-FRI *)"
        # )
        # rule.add_target(targets.LambdaFunction(lambdaFn))

app = cdk.App()
LambdaCronStack(app, "cdk-lambda-cdk-1")
app.run()


# app = cdk.App()
# CdkLambdaStack(app, "cdk-lambda-cdk-1")
#
# app.run()
