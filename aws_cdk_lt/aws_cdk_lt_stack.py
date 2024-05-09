from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources,
)
from constructs import Construct

function_timeout = 3
function_memory_size = 128

class AwsCdkLtStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_function = lambda_.Function(self, "HelloWorldFunction",
            code=lambda_.Code.from_asset("lib"),
            handler="lambda_handler.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_8,
            timeout=Duration.minutes(function_timeout),
            memory_size=function_memory_size,
        )
        lambda_function.add_event_source(lambda_event_sources.ApiEventSource(
                method="get",
                path="/hello",
            )
        )
