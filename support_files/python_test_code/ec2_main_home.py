import streamlit as st
import boto3
import psutil
import requests


st.set_page_config(
    page_title='CJ OliveNetworks CloudWave', 
    page_icon=None, 
    layout="wide", 
    initial_sidebar_state="expanded", 
    menu_items=None
)


st.title("AWS EC2 Information")
st.header('EC2 Instance Information Table', divider = "gray")
cole1, cole2 = st.columns([3, 7])

def get_token():
    url = "http://169.254.169.254/latest/api/token"
    headers = {"X-aws-ec2-metadata-token-ttl-seconds": "3600"}
    response = requests.put(url, headers=headers)
    return response.text

def get_instance_metadata(token, endpoint):
    url = f"http://169.254.169.254/latest/meta-data/{endpoint}"
    headers = {"X-aws-ec2-metadata-token": token}
    response = requests.get(url, headers=headers)
    return response.text

def get_instance_name_tag(ec2_client, instance_id):
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # 태그 목록 내에서 'Name' 키를 가진 태그를 찾습니다.
            name_tag = next((tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'), None)
            if name_tag:
                return name_tag  # 'Name' 태그 값 반환
    return None

# EC2 Information
token = get_token()

instance_id=get_instance_metadata(token, "instance-id")
instance_type=get_instance_metadata(token, "instance-type")
instance_region=get_instance_metadata(token, "placement/region")
instance_availability_zone=get_instance_metadata(token, "placement/availability-zone")
instance_private_ip=get_instance_metadata(token, "local-ipv4")
instance_public_ip=get_instance_metadata(token, "public-ipv4")

ec2_client = boto3.client('ec2', region_name=instance_region)
instance_name = get_instance_name_tag(ec2_client, instance_id)

with cole1:
    st.subheader(":black_small_square: Instance Name: ")
    st.subheader(":black_small_square: Instance ID: ")
    st.subheader(":black_small_square: Instance Type: ")
    st.subheader(":black_small_square: Region: ")
    st.subheader(":black_small_square: Availabiltiry Zone: ")
    st.subheader(":black_small_square: Private IP: ")
    st.subheader(":black_small_square: Public IP: ")
with cole2:
    st.subheader(instance_name)
    st.subheader(instance_id)
    st.subheader(instance_type)
    st.subheader(f":green[{instance_region}]")
    st.subheader(instance_availability_zone)
    st.subheader(instance_private_ip)
    st.subheader(instance_public_ip)
