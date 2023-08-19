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


## Invoke using scheduler


To invoke a function once a day using Amazon EventBridge (formerly known as Amazon CloudWatch Events), you can use the following steps:

1. **Create or identify the target resource (e.g., Lambda function)**:
   - If you don't already have a Lambda function, create one using the AWS Management Console or AWS CLI.
   - Make sure your Lambda function has the appropriate permissions to be triggered by Amazon EventBridge.

2. **Create an IAM role (if necessary)**:
   - If you don't already have an IAM role that grants EventBridge permission to trigger your Lambda function, create one.
   - The role should have the `AWSLambda_ReadOnlyAccess` and `AWSLambda_FullAccess` policies attached, or equivalent permissions.
   - The trust policy should allow EventBridge to assume the role.

3. **Create an EventBridge rule**:
   - In the AWS Management Console, navigate to the Amazon EventBridge service.
   - Go to the "Rules" section and click the "Create rule" button.
   - Enter a name and description for your rule.
   - In the "Define pattern" section, choose "Schedule".
   - Select "Cron expression" and enter a cron expression that corresponds to once a day at your desired time. For example, to run the function every day at 12:00 PM UTC, enter `0 12 * * ? *`.

4. **Configure the target**:
   - In the "Select targets" section, choose "Lambda function" as the target type.
   - Select your Lambda function from the drop-down list.
   - If you created an IAM role in step 2, select it as the "Existing role" under "Create a new role or select an existing role".

5. **Configure input**:
   - If your function requires specific input, configure the input for the target in the "Configure input" section.

6. **Create the rule**:
   - Click the "Create" button at the bottom of the page to create the rule.

7. **Verify the rule**:
   - Ensure that the rule appears in the list of rules in the EventBridge console.
   - Verify that your function is being invoked as expected by checking the CloudWatch Logs for your Lambda function or any other monitoring solution you have in place.

That's it! Your Lambda function should now be automatically invoked once a day at the specified time.

Keep in mind that Amazon EventBridge uses the UTC time zone by default. You may need to adjust the cron expression if you want the function to run at a specific time in a different time zone.
