import boto3

def get_dynamodb():
    return boto3.resource(
        "dynamodb",
        region_name="us-east-1",
        endpoint_url="http://localhost:8001",
        aws_access_key_id="dummy",
        aws_secret_access_key="dummy"
    )
