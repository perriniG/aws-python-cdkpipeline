Summary
This pattern describes how to automatically create the continuous integration and continuous delivery (CI/CD) pipelines and underlying infrastructure for building and deploying microservices on Amazon Elastic Container Service (Amazon ECS). You can use this approach if you want to set up proof-of-concept CI/CD pipelines to show your organization the benefits of CI/CD, microservices, and DevOps. You can also use this approach to create initial CI/CD pipelines that you can then customize or change according to your organization’s requirements. 

The pattern’s approach creates a production environment and non-production environment that each have a virtual private cloud (VPC) and an Amazon ECS cluster configured to run in two Availability Zones. These environments are shared by all your microservices and you then create a CI/CD pipeline for each microservice. These CI/CD pipelines pull changes from a source repository in AWS CodeCommit, automatically build the changes, and then deploy them into your production and non-production environments. When a pipeline successfully completes all of its stages, you can use URLs to access the microservice in the production and non-production environments.

Prerequisites and limitations
Prerequisites 

An active Amazon Web Services (AWS) account.

An existing Amazon Simple Storage Service (Amazon S3) bucket that contains the starter-code.zip file (attached).

AWS Cloud Development Kit (AWS CDK), installed and configured in your account. For more information about this, see Getting started with the AWS CDK in the AWS CDK documentation.

Python 3 and pip, installed and configured. For more information about this, see the Python documentation.

Familiarity with AWS CDK, AWS CodePipeline, AWS CodeBuild, CodeCommit, Amazon Elastic Container Registry (Amazon ECR), Amazon ECS, and AWS Fargate.

Familiarity with Docker.

An understanding of CI/CD and DevOps.

Limitations

General AWS account limits apply. For more information about this, see AWS service quotas in the AWS General Reference documentation.

Product versions

The code was tested using Node.js version 16.13.0 and AWS CDK version 1.132.0.
Resource:
https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-build-ci-cd-pipelines-and-amazon-ecs-clusters-for-microservices-using-aws-cdk.html
