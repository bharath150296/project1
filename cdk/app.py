#!/usr/bin/env python3
import aws_cdk as cdk
from project1_stack import Project1Stack

app = cdk.App()
Project1Stack(app, "Project1Stack")
app.synth()
