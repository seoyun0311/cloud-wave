# Ubuntu - PostgreSQL v.15 install 

# PostgreSQL 공식 저장소 추가
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# 시스템 패키지 업데이트
sudo apt update

# PostgreSQL 설치
sudo apt install postgresql-15 postgresql-server-dev-15 -y

# PostgreSQL Dev Tool 설치
sudo apt install python3-psycopg2

# 사용자 전환
# postgres 사용자로 전환하면 Data Directory에 접근할 수 있지만, 다른 사용자는 생성할 수 없습니다.
sudo -i -u postgres