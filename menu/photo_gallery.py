import io
import boto3
import requests
import streamlit as st

from PIL import Image

class PhotoGallery:
    def __init__(self):
        self.main_page()
        
    def get_token(self):
        url = "http://169.254.169.254/latest/api/token"
        headers = {"X-aws-ec2-metadata-token-ttl-seconds": "3600"}
        response = requests.put(url, headers=headers)
        return response.text
    
    def get_instance_metadata(self, token, endpoint):
        url = f"http://169.254.169.254/latest/meta-data/{endpoint}"
        headers = {"X-aws-ec2-metadata-token": token}
        response = requests.get(url, headers=headers)
        return response.text
        
    def get_account_id(self, token):
        url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
        headers = {"X-aws-ec2-metadata-token": token}
        response = requests.get(url, headers=headers)
        res = response.json()
        return res.get('accountId')
    
    def list_s3_object(self, sdk, bucket):
        files = []
        response = sdk.list_objects(Bucket=bucket)
        for obj in response.get('Contents', []):
            files.append(obj['Key'])
        return files
        
    def load_image(self, sdk, bucket, key):
        response = sdk.get_object(Bucket=bucket, Key=key)
        image_bytes = response['Body'].read()
        img = Image.open(io.BytesIO(image_bytes))
        return img
    
    def main_page(self):
        st.title("Animal Pictures")
        st.header('Puppy Pictures', divider = "gray")
        token = self.get_token()
        region = self.get_instance_metadata(token, "placement/region")
        
        accountId = self.get_account_id(token)
        bucket_name = f"lab-edu-bucket-image-{accountId}"
        
        s3 = boto3.client('s3', region_name=region)
        object_list = self.list_s3_object(s3, bucket_name)

        columns_per_row = 3
        # range(start, end, increase)
        for index in range(0, len(object_list), columns_per_row):
            # Split a web page using 'st.columns' to display three image in one row
            cols = st.columns(columns_per_row)
            for i in range(columns_per_row):
                with cols[i]:
                    if index + i < len(object_list) and object_list[index+i].lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        dog_name=object_list[index+i].split(".")[0]
                        st.subheader(dog_name)
                        # Use the 'endswith' Method to check whether image file or not
                        
                        image = self.load_image(s3, bucket_name, object_list[index+i])
                        st.image(image, use_column_width=True)
                        # st.image(image)
