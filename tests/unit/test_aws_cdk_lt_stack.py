import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_lt.aws_cdk_lt_stack import AwsCdkLtStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_lt/aws_cdk_lt_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkLtStack(app, "aws-cdk-lt")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
