from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class Project1Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        _lambda.Function(
            self,
            "Project1Lambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("../lambda.zip"),
        )
