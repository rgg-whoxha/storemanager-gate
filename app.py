import aws_cdk as cdk
from storemanager_gate_stack import StoremanagerStack

app = cdk.App()
StoremanagerStack(app, "StoremanagerStack")

app.synth()
