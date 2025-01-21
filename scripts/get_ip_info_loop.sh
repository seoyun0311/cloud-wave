#!/bin/bash
# WRITER INSTANCE
while true; do 
  nslookup {RDS_AURORA_WRITER_ENDPOINT} | grep -E "Address: 10\." | awk '{print $2}';
  sleep 1; 
done

# READER INSTANCE
while true; do 
  nslookup {RDS_AURORA_READER_ENDPOINT} | grep -E "Address: 10\." | awk '{print $2}';
  sleep 1; 
done