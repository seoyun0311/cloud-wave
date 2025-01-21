#!/bin/bash

# variable
INPUT_FILE="/Workshop/support_files/policy/s3_bucket_policy_endpoint.json"
OUTPUT_FILE="/Workshop/support_files/policy/s3_bucket_policy_endpoint_output.json"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
BUCKET_ARN="arn:aws:s3:::lab-edu-bucket-image-$ACCOUNT_ID"
IAM_ROLE_ARN=$(aws iam get-role --role-name lab-edu-role-ec2 --query 'Role.Arn' --output text)
VPC_ENDPOINT_ID=$(aws ec2 describe-vpc-endpoints --filters "Name=tag:Name,Values=lab-edu-endpoint-s3" --query "VpcEndpoints[*].VpcEndpointId" --output text)


# copy file
cp "$INPUT_FILE" "$OUTPUT_FILE"

# convert placeholder
sed -i "s|{IAM_ROLE_ARN}|$IAM_ROLE_ARN|g" $OUTPUT_FILE
sed -i "s|{BUCKET_ARN}|$BUCKET_ARN|g" $OUTPUT_FILE
sed -i "s|{VPC_ENDPOINT_ID}|$VPC_ENDPOINT_ID|g" $OUTPUT_FILE

# print outcome
echo "Contents of $OUTPUT_FILE: \n"
cat "$OUTPUT_FILE"