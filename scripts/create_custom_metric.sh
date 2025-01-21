#!/bin/bash

# variable
REGION="ap-northeast-2"               # AWS region
NAMESPACE="Custom/DiskMetrics"        # CloudWatch custom namespace information
METRIC_NAME="DiskSpaceUtilization"    # metric name
DIMENSION_NAME="MountPath"            # dimension name
MOUNT_PATH="/"                        # directory path
TOKEN=$(curl --request PUT "http://169.254.169.254/latest/api/token" --header "X-aws-ec2-metadata-token-ttl-seconds: 3600")
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id --header "X-aws-ec2-metadata-token: $TOKEN")

# collect disk usage metric 
DISK_USAGE=$(df -h $MOUNT_PATH | grep -v 'Filesystem' | awk '{print $5}' | sed 's/%//')

# push metric data to CloudWatch
aws cloudwatch put-metric-data \
  --metric-name $METRIC_NAME \
  --namespace $NAMESPACE \
  --dimensions InstanceId=$INSTANCE_ID,$DIMENSION_NAME=$MOUNT_PATH \
  --value $DISK_USAGE \
  --unit Percent \
  --region $REGION

echo "Disk usage ($DISK_USAGE%) for $MOUNT_PATH sent to CloudWatch in $REGION"