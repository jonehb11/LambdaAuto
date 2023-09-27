# AWS Lambda Blackhole Routes Detector

![AWS Logo](https://raw.githubusercontent.com/github/explore/master/topics/aws/aws.png)

## Overview

This is a fun weekend project that involves using AWS Lambda, AWS Secrets Manager, Amazon EC2, Amazon SNS, and Amazon EventBridge. The project's main goal is to identify "blackhole" routes in route tables across all VPCs in your AWS account and send a consolidated report to an SNS topic.

The Lambda function is written in Python and utilizes the `boto3` library to interact with AWS services securely. It retrieves credentials from AWS Secrets Manager, scans through the route tables, identifies blackhole routes, and sends a comprehensive report to an SNS topic. The project showcases the power of serverless computing and AWS's rich service ecosystem.

## Features

- Securely retrieves AWS credentials using AWS Secrets Manager.
- Scans route tables across all VPCs to identify blackhole routes.
- Consolidates blackhole route instances into a single report.
- Sends the report as a message to an SNS topic.
- Utilizes Amazon EventBridge Scheduler to automatically invoke the function daily.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/aws-lambda-blackhole-detector.git





## Step 1: Creating an SNS Topic

1. Open the [Amazon SNS Console](https://console.aws.amazon.com/sns).
2. In the SNS dashboard, click on "Create topic".
3. Choose "Standard" as the type of the topic.
4. Enter a name and display name for the topic.
5. Click "Create topic".

You will see the ARN for your newly created topic in the SNS dashboard.

## Step 2: Create a Secret in Secrets Manager

1. Open the [AWS Secrets Manager Console](https://console.aws.amazon.com/secretsmanager).
2. Click "Create a new secret".
3. Choose "Other types of secrets".
4. In the key-value pair, input `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as the keys and provide your AWS Access Key ID and Secret Access Key as the values, respectively.
5. Click "Next".
6. Give your secret a name.
7. Click "Next" and review the secret.
8. Click "Create secret".

## Step 3: Create a Lambda Function

1. Open the [AWS Lambda Console](https://console.aws.amazon.com/lambda).
2. Click "Create function".
3. Choose "Author from scratch".
4. Name your function and choose a runtime (e.g. Python 3.8).
5. Under "Execution role", create a new role with basic permissions.
6. Click "Create function".

## Step 4: Create EventBridge Rule to Invoke Lambda Function

1. Open the [Amazon EventBridge Console](https://console.aws.amazon.com/events).
2. Click "Create rule".
3. Give your rule a name.
4. In the "Event Source" section, choose "Schedule". In the cron or rate expression field, enter `rate(1 day)` to run it once a day.
5. In the "Targets" section, choose "Lambda function" from the dropdown menu and select your previously created Lambda function.
6. Click "Create".

Once you have completed these steps, your Lambda function will be triggered once a day by the EventBridge rule. When triggered, the Lambda function will publish a message to the SNS topic.

**Note:** Make sure your Lambda function has appropriate permissions to access the SNS topic, Secrets Manager, and EventBridge. You can do this by adding the necessary permissions to the execution role of your Lambda function. Also, ensure that the AWS credentials stored in the Secrets Manager are valid and have permissions to perform the necessary actions.
