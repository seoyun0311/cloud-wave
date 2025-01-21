#!/bin/bash
# JSON 파일 경로
JSON_PATH="JSON_FILE"

# Check if the folder exists
if [ ! -d "$JSON_PATH" ]; then
    # Folder doesn't exist, so create it
    mkdir "$JSON_PATH"
    echo "Created folder: $JSON_PATH"
else
    # Folder exists
    echo "Folder $JSON_PATH already exists."
fi
RECORD_NAME=$1
ZONE_NAME="cj-cloud-wave.com."
ZONE_ID=$(aws route53 list-hosted-zones --query "HostedZones[?Name == '$RECORD_NAME.$ZONE_NAME'].Id" --output text)
JSON_DIR="JSON_FILE"/$RECORD_NAME.json
cp ns_record_sample.json $JSON_DIR

# NS 레코드 캡처
NS_RECORDS=($(aws route53 list-resource-record-sets --hosted-zone-id $ZONE_ID --query "ResourceRecordSets[?Type == 'NS' && Name == '$RECORD_NAME.$ZONE_NAME'].ResourceRecords[].Value" --output text))

# JSON 파일 업데이트
jq --arg ns1 "${NS_RECORDS[0]}" \
--arg ns2 "${NS_RECORDS[1]}" \
--arg ns3 "${NS_RECORDS[2]}" \
--arg ns4 "${NS_RECORDS[3]}" \
--arg recordName "$RECORD_NAME.$ZONE_NAME" \
'.Changes[0].ResourceRecordSet.Name = $recordName |
.Changes[0].ResourceRecordSet.ResourceRecords[0].Value = $ns1 |
.Changes[0].ResourceRecordSet.ResourceRecords[1].Value = $ns2 |
.Changes[0].ResourceRecordSet.ResourceRecords[2].Value = $ns3 |
.Changes[0].ResourceRecordSet.ResourceRecords[3].Value = $ns4' $JSON_DIR > temp.json && mv temp.json $JSON_DIR
