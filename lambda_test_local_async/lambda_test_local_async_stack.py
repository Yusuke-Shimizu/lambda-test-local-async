from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
import aws_cdk.aws_lambda as lambda_
from aws_cdk.aws_lambda_python import PythonFunction
from aws_cdk.aws_apigateway import LambdaIntegration, RestApi


class LambdaTestLocalAsyncStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        lambda_function = PythonFunction(self, "MyFunction",
            entry="src", # required
            index="sync.py", # optional, defaults to 'index.py'
            handler="handler", # optional, defaults to 'handler'
            runtime=lambda_.Runtime.PYTHON_3_7
        )

        api = RestApi(self, "api")
        api.root.add_method("GET", LambdaIntegration(lambda_function))
