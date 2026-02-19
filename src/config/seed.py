import boto3

dynamodb = boto3.client(
    "dynamodb",
    region_name="us-east-1",
    endpoint_url="http://localhost:8001",
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy"
)
try:
    dynamodb.create_table(
        TableName="appointments",
        KeySchema=[
            {"AttributeName": "PK", "KeyType": "HASH"},
            {"AttributeName": "SK", "KeyType": "RANGE"}
        ],
        AttributeDefinitions=[
            {"AttributeName": "PK", "AttributeType": "S"},
            {"AttributeName": "SK", "AttributeType": "S"}
        ],
        BillingMode="PAY_PER_REQUEST"
    )
except dynamodb.exceptions.ResourceInUseException:
    print("La tabla ya existe, saltando creación... ✅")
