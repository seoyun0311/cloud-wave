#!/bin/bash

# 설정
BUCKET_NAME="your-bucket-name"
FILE_NAME="your-large-file"
OBJECT_KEY="your-object-key"
PART_SIZE="5M"

# 파일 분할
split -b $PART_SIZE $FILE_NAME ${FILE_NAME}-part-

# Multipart upload 시작
UPLOAD_ID=$(aws s3api create-multipart-upload --bucket $BUCKET_NAME --key $OBJECT_KEY --output text --query 'UploadId')
echo "Multipart upload started with UploadId: $UPLOAD_ID"

# 각 부분 업로드
PART_NUMBER=1
ETAGS=()

for PART in ${FILE_NAME}-part-*
do
    echo "Uploading part $PART_NUMBER: $PART"
    ETAG=$(aws s3api upload-part --bucket $BUCKET_NAME --key $OBJECT_KEY --part-number $PART_NUMBER --body $PART --upload-id $UPLOAD_ID --output text --query 'ETag')
    ETAGS+=("{\"ETag\":$ETAG,\"PartNumber\":$PART_NUMBER}")
    PART_NUMBER=$((PART_NUMBER + 1))
done

# Multipart upload 완료를 위한 JSON 생성
JSON_PARTS=$(IFS=,; echo "${ETAGS[*]}")
JSON_BODY="{\"Parts\":[$JSON_PARTS]}"
echo $JSON_BODY > multipart.json

# Multipart upload 완료
aws s3api complete-multipart-upload --bucket $BUCKET_NAME --key $OBJECT_KEY --upload-id $UPLOAD_ID --multipart-upload file://multipart.json

# 임시 파일 정리
rm ${FILE_NAME}-part-*
rm multipart.json

echo "Multipart upload completed successfully"