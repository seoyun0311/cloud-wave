import boto3
import json
import psycopg2

def get_secret_value(secret_name, region_name):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)
        if 'SecretString' in response:
            return json.loads(response['SecretString'])
        else:
            raise Exception("Secret value not found.")
    except Exception as e:
        raise Exception(f"Failed to retrieve secret value: {e}")
    

def connect_to_database(secret_values):
    host = secret_values['host']
    port = secret_values['port']
    database = secret_values['database']
    username = secret_values['username']
    password = secret_values['password']
    # print(host,port,database,username,password)

    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database
        )
        return connection
    except Exception as e:
        raise Exception(f"Failed to connect to the database: {e}")
    

def get_db_connection():
    # Replace with your AWS region
    aws_region = "REGION"
    # aws_region = "ap-northeast-2"

    # Replace with your secret name in AWS Secret Manager
    secret_name = "SECRETS_NAME"
    # secret_name = "/secret/aurora"

    try:
        secret_values = get_secret_value(secret_name, aws_region)
        return connect_to_database(secret_values)
    except Exception as e:
        print(f"Error: {e}")
