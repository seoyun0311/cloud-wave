#!/bin/bash

# variable
INPUT_FILE="/Workshop/support_files/policy/s3_bucket_policy_ec2_web_ip.json"
OUTPUT_FILE="/Workshop/support_files/policy/s3_bucket_policy_ec2_web_ip_output.json"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
BUCKET_NAME="lab-edu-bucket-image-$ACCOUNT_ID"
BUCKET_ARN="arn:aws:s3:::lab-edu-bucket-image-$ACCOUNT_ID"
VPC_ID=$(aws ec2 describe-vpcs --filters "Name=tag:Name,Values=lab-edu-vpc-ap-01" --query 'Vpcs[0].VpcId' --output text)
NAT_GATEWAY_PUBLIC_IP=$(aws ec2 describe-nat-gateways --filter Name=vpc-id,Values=$VPC_ID --query 'NatGateways[*].NatGatewayAddresses[0].PublicIp' --output text)

# copy file
cp "$INPUT_FILE" "$OUTPUT_FILE"

# convert placeholder
sed -i "s|{BUCKET_ARN}|$BUCKET_ARN|g" $OUTPUT_FILE
sed -i "s|{NAT_GATEWAY_PUBLIC_IP}|$NAT_GATEWAY_PUBLIC_IP|g" $OUTPUT_FILE

# print outcome
echo "Contents of $OUTPUT_FILE: \n"
cat "$OUTPUT_FILE"

aws s3api put-bucket-policy --bucket $BUCKET_NAME --policy file://$OUTPUT_FILE