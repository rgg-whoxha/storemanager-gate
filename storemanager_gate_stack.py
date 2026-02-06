from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_apigateway as apigw
)
from constructs import Construct

class StoremanagerStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table = dynamodb.Table(
            self, "user_permissions",
            partition_key=dynamodb.Attribute(name="username", type=dynamodb.AttributeType.STRING)
        )

        storemanager_lambda = _lambda.Function(
            self, "user_permissions_handler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="main.handler", 
            code=_lambda.Code.from_asset(".")          )

        table.grant_read_write_data(storemanager_lambda)

        apigw.LambdaRestApi(
            self, "storemanagerGateEndpoint",
            handler=storemanager_lambda
        )