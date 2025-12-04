# project1 — Lambda + CDK Deployment

This project automatically builds and deploys an AWS Lambda function using:

- AWS CodePipeline
- AWS CodeBuild
- AWS CDK
- Python 3.12

## Deployment Flow

1. CodePipeline pulls code from GitHub/CodeCommit
2. CodeBuild:
   - Installs dependencies
   - Packages Lambda into lambda.zip
   - Deploys CDK stack
3. CDK deploys Lambda to AWS
