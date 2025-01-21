#!/bin/bash


terminate_process() {
  local PIDS=$1
  local NAME=$2
  local NOW=$(date "+%Y %b %d %a %H:%M:%S")
  local STOP_LOG="/var/log/codedeploy_$NAME.log"

  if [ -z "$PIDS" ]; then
    echo "[$NOW] $NAME is not running" >> $STOP_LOG
  else
    echo "[$NOW] 기존 프로세스 종료 시도: PID $PIDS" >> $STOP_LOG
    for PID in $PIDS; do
      echo "Kill -9 $PID ($NAME)"
      kill -9 $PID
      sleep 1
    done
  fi
}

# Find PIDs
APP_PID=$(pgrep streamlit)
FLASK_PIDS=$(pgrep -f "python app.py")

# Terminate processes
terminate_process "$APP_PID" "streamlit"
terminate_process "$FLASK_PIDS" "flask"

sleep 5
exit 0