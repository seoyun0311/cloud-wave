#!/bin/bash

# variable
INPUT_FILE="/Workshop/support_files/policy/s3_bucket_policy_ec2_web_role.json"
OUTPUT_FILE="/Workshop/support_files/policy/s3_bucket_policy_ec2_web_role_output.json"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
BUCKET_ARN="arn:aws:s3:::lab-edu-bucket-image-$ACCOUNT_ID"
IAM_ROLE_ARN=$(aws iam get-role --role-name lab-edu-role-ec2 --query 'Role.Arn' --output text)

# copy file
cp "$INPUT_FILE" "$OUTPUT_FILE"

# convert placeholder
sed -i "s|{ACCOUNT_ID}|$ACCOUNT_ID|g" $OUTPUT_FILE
sed -i "s|{IAM_ROLE_ARN}|$IAM_ROLE_ARN|g" $OUTPUT_FILE
sed -i "s|{BUCKET_ARN}|$BUCKET_ARN|g" $OUTPUT_FILE

# print outcome
echo "Contents of $OUTPUT_FILE: \n"
cat "$OUTPUT_FILE"