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


