import boto3
import json 

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    #print(event)
    bucket_name = event.get("Records")[0].get("s3").get("bucket").get("name")
    print(f"Print the bucket employees data uploaded: {bucket_name}")
    file_name = event.get("Records")[0].get("s3").get("object").get("key")
    print(f"Retrieve file name from: {bucket_name} and filename: {file_name}")
    json_object = s3_client.get_object(Bucket=bucket_name,Key=file_name)
    json_file_reader = json_object["Body"].read()
    # print(f"Read the content of json file: {json_file_reader}")
    # print(type(json_file_reader))
    #Convert the byte file to dictionary 
    json_dict = json.loads(json_file_reader)
    #print(type(json_dict))
    table = dynamodb.Table('Employees')
    table.put_item(Item=json_dict)