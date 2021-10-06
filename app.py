#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from lambda_test_local_async.lambda_test_local_async_stack import LambdaTestLocalAsyncStack


app = core.App()
env = app.node.try_get_context("env")
LambdaTestLocalAsyncStack(app, "LambdaTestLocalAsyncStack-" + env)

app.synth()
