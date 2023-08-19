import os
import json
import boto3
from botocore.exceptions import NoCredentialsError

def lambda_handler(event, context):
    secret_name = "examplecred"  # Replace with your secret name
    region_name = "us-east-1"  # Replace with the correct region of your secret
    sns_topic_arn = "arn:aws:sns:us-east-1:12345"  # Replace with the ARN of your SNS topic

    # Create a Secrets Manager client
    secrets_client = boto3.client("secretsmanager", region_name=region_name)

    try:
        # Retrieve the secret value
        response = secrets_client.get_secret_value(SecretId=secret_name)
        secret_value = json.loads(response["SecretString"])

        aws_access_key_id = secret_value["AWS_ACCESS_KEY_ID"]
        aws_secret_access_key = secret_value["AWS_SECRET_ACCESS_KEY"]
        aws_region = secret_value["AWS_REGION"]

        # Use the retrieved credentials to create the AWS SDK clients
        ec2_client = boto3.client(
            "ec2",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region,
        )
        sns_client = boto3.client(
            "sns",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region,
        )

        # check all route tables in account/pull vpc info/route status
        rtbls = ec2_client.describe_route_tables()
        blkholelst = []
        for item in rtbls['RouteTables']:
            rtb_id = item['RouteTableId']
            AssoVpc = item['VpcId']
        
            for item3 in item['Routes']:
                blkhole = item3['State']
                if blkhole == 'blackhole':
                    message_body = 'VpcId:{}:route table:{} - {}'.format(AssoVpc, rtb_id, blkhole)
                    blkholelst.append(message_body)

        # Publish message to the SNS topic/convert list into string 
        convert = ','.join(blkholelst)
        sns_client.publish(
                TopicArn=sns_topic_arn,
                Message=convert
                )

        print("Published message to SNS topic: {}".format(convert))

    except NoCredentialsError as e:
        print("Error: Failed to retrieve credentials from Secrets Manager")
        raise e
