#!/bin/bash
# Variables
FILE_NAME="network_baseline.yaml"
STACK_NAME="lab-edu-cf-network-baseline-us"
REGION="us-east-1"

# Check if the file exists
if [ ! -f "$FILE_NAME" ]; then
  echo "Error: Template file '$FILE_NAME' not found."
  exit 1
fi

# Create CloudFormation stack
aws cloudformation create-stack --stack-name $STACK_NAME \
--template-body file://$FILE_NAME \
--capabilities CAPABILITY_NAMED_IAM \
--region $REGION \
--parameters \
ParameterKey=AvailabilityZoneSubnet01,ParameterValue=${REGION}a \
ParameterKey=AvailabilityZoneSubnet02,ParameterValue=${REGION}c

# Check for success
if [ $? -eq 0 ]; then
  echo "CloudFormation stack '$STACK_NAME' created successfully."
else
  echo "Failed to create the CloudFormation stack: $STACK_NAME"
  exit 1
fi