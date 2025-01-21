#!/bin/bash
ZONE_NAME="cj-cloud-wave.com."
ZONE_ID=$(aws route53 list-hosted-zones --query "HostedZones[?Name == '$ZONE_NAME'].Id" --output text)
JSON_DIR="JSON_FILE"

json_files=("$JSON_DIR"/*.json)
echo "JSON files found in the directory:"
for file in "${json_files[@]}"; do
    echo "$file"
done

for json_file in "${json_files[@]}"; do
    if [ -f "$json_file" ]; then
        echo "Applying changes from $json_file"
        aws route53 change-resource-record-sets --hosted-zone-id $ZONE_ID --change-batch file://"$json_file"
    fi
done