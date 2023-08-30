import json
import boto3
s3_client = boto3.client('s3')
dyna = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file = event['Records'][0]['s3']['object']['key']
    obj = s3_client.get_object(Bucket=bucket,Key=json_file)
    jsonfile = obj['Body'].read()
    json2py = json.loads(jsonfile)
    table = dyna.Table('employees')
    table.put_item(Item=json2py)
    print(bucket)
    print(json_file)
    print(str(event))