import aws_cdk as core
import aws_cdk.assertions as assertions

from account_provisioning_infrastructure.account_provisioning_infrastructure_stack import AccountProvisioningInfrastructureStack

# example tests. To run these tests, uncomment this file along with the example
# resource in account_provisioning_infrastructure/account_provisioning_infrastructure_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AccountProvisioningInfrastructureStack(app, "account-provisioning-infrastructure")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
