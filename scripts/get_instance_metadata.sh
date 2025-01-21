#!/bin/bash

TOKEN=$(curl --request PUT "http://169.254.169.254/latest/api/token" --header "X-aws-ec2-metadata-token-ttl-seconds: 3600")
#echo $TOKEN

INSTANCE_METADATA=$(curl -s http://169.254.169.254/latest/meta-data/ --header "X-aws-ec2-metadata-token: $TOKEN")
#echo $INSTANCE_METADATA

INSTANCE_HOSTNAME=$(curl -s http://169.254.169.254/latest/meta-data/hostname --header "X-aws-ec2-metadata-token: $TOKEN")
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id --header "X-aws-ec2-metadata-token: $TOKEN")
INSTANCE_TYPE=$(curl -s http://169.254.169.254/latest/meta-data/instance-type --header "X-aws-ec2-metadata-token: $TOKEN")
INSTANCE_REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/region --header "X-aws-ec2-metadata-token: $TOKEN")
INSTANCE_HOSTNAME=$(curl -s http://169.254.169.254/latest/meta-data/hostname --header "X-aws-ec2-metadata-token: $TOKEN")
INSTANCE_PRIVATE_IP=$(curl -s http://169.254.169.254/latest/meta-data/local-ipv4 --header "X-aws-ec2-metadata-token: $TOKEN")
INSTANCE_PUBLIC_IP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4 --header "X-aws-ec2-metadata-token: $TOKEN")
INSTANCE_AVAILABILITY_ZONE=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone --header "X-aws-ec2-metadata-token: $TOKEN")

echo $INSTANCE_HOSTNAME
echo $INSTANCE_ID
echo $INSTANCE_TYPE
echo $INSTANCE_REGION
echo $INSTANCE_HOSTNAME
echo $INSTANCE_PRIVATE_IP
echo $INSTANCE_PUBLIC_IP
echo $INSTANCE_AVAILABILITY_ZONE
