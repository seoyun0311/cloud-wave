#!/bin/bash

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
BUCKET_NAME="lab-edu-bucket-image-${ACCOUNT_ID}-backup"

aws s3api list-object-versions --bucket $BUCKET_NAME --query 'DeleteMarkers[].{Key:Key,VersionId:VersionId}' --output json | jq -c '.[]' | while read -r object; do
    KEY=$(echo $object | jq -r '.Key')
    VERSION_ID=$(echo $object | jq -r '.VersionId')
    aws s3api delete-object --bucket $BUCKET_NAME --key "$KEY" --version-id "$VERSION_ID"
    echo "Removed delete marker for $KEY (Version ID: $VERSION_ID)"
done