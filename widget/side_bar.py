import subprocess

def stop_process():
    process_cmd = "kill -9 $(ps -ef | grep stress | grep -v grep | awk '{print $2}' | sed -n '2p')"
    subprocess.run(process_cmd, shell=True)

def start_process(timeout=300):
    stop_process()  # 새 프로세스를 시작하기 전에 이전 프로세스를 종료합니다.
    command = f"stress --cpu 2 --timeout {timeout}"
    subprocess.Popen(command, start_new_session=True, shell=True)