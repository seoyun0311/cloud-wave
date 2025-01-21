SELECT
 useridentity.arn,
 eventname,
 sourceipaddress,
 eventtime
FROM {CLOUDTRAIL_LOGS}
LIMIT 100;
