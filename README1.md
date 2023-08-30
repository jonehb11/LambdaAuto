# AWS Lambda: Trigger from S3 to DynamoDB on JSON Upload

## Objective
Create an AWS Lambda function that is triggered when a new JSON object is added to an AWS S3 bucket. The function will process the uploaded JSON file and populate a DynamoDB table with its contents.

## Requirements
- AWS Account
- AWS CLI configured
- Python with Boto3 installed
- Familiarity with AWS S3, AWS Lambda, and AWS DynamoDB

## Step-by-Step Guide

### 1. Prepare S3 Bucket
- Navigate to AWS S3 Console and create a new bucket, or use an existing one where the JSON files will be uploaded.

### 2. Initialize DynamoDB Table
- Go to the AWS DynamoDB Console and create a new table that will hold the processed data from the JSON files. Note the table name for use in your Lambda function.

### 3. Create IAM Role
- Open AWS IAM Console and create a new role.
- Attach policies granting read access to the S3 bucket and full access to the DynamoDB table.

### 4. Develop Lambda Function
- Head over to the AWS Lambda Console and create a new function.
- Assign the IAM role you've created to this function.
- Upload the  Python code s3todynamodb.py file to lambda. This code reads a JSON file from the S3 bucket, processes it, and uploads its contents into a DynamoDB table.



### 5. Configure S3 Trigger
- Under the "Configuration" tab of your Lambda function, click "Add Trigger."
- Select "S3" from the trigger type dropdown.
- Configure the trigger to activate on a "PUT" event on the S3 bucket where you'll upload the JSON files.

### 6. Validate Workflow
- Upload a sample JSON file to your S3 bucket.
- Verify that the Lambda function is triggered and the data is inserted into your DynamoDB table.

And that's it! You have successfully created a Lambda function that is triggered by the upload of a JSON file to an S3 bucket and populates a DynamoDB table with the file's contents.
