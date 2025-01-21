#!/bin/bash
while true; do
  PGPASSWORD="qwer1234" psql -h {RDS_AURORA_READER_ENDPOINT} \
       -U user \
       -d trip_advisor \
       -c "select * from attractions;";
  sleep 10;
done