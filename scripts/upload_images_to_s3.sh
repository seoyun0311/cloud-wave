#!/bin/bash

# Get AccountId Value
TOKEN=$(curl --request PUT "http://169.254.169.254/latest/api/token" --header "X-aws-ec2-metadata-token-ttl-seconds: 3600")
ACCOUNT_ID=$(curl -s http://169.254.169.254/latest/dynamic/instance-identity/document --header "X-aws-ec2-metadata-token: $TOKEN" | jq -r .accountId)

# Relative path based on the Cloud9 'environment' directory
BUCKET_NAME="lab-edu-bucket-image-$ACCOUNT_ID"
FOLDER_PATH="cloud-wave-workspace/images/animal_picture/"

aws s3 mb "s3://$BUCKET_NAME"
aws s3 cp "$FOLDER_PATH" "s3://$BUCKET_NAME/" --recursive