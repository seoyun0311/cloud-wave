import json
import boto3
from botocore.exceptions import ClientError

# DynamoDB 리소스 초기화
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('lab-edu-dynamodb-todo-list')  # DynamoDB 테이블 이름으로 대체

def lambda_handler(event, context):
    try:
        todo = event['todo']
    except (KeyError, TypeError, json.JSONDecodeError):
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid request')
        }
    table.put_item(Item={'todo': todo})    
    
    try:
        response = table.scan()
        items = response['Items']
        print(items)
        data = {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(items)
        }
        return data
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error retrieving data from DynamoDB: ' + str(e))
        }