import json
import boto3

# DynamoDB 초기화
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('lab-edu-dynamodb-todo-list')

def lambda_handler(event, context):
    try:
        # 요청 본문에서 삭제할 항목의 키 추출
        todo = event['todo']

        # DynamoDB에서 항목 삭제
        table.delete_item(
            Key={'todo': todo}
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Item deleted successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error deleting item')
        }