# Amazon Linux 2023 - PostgreSQL v.15 install 
# PostgreSQL Install
sudo dnf update -y
sudo dnf install postgresql15  -y
sudo dnf install postgresql15-server -y
sudo dnf install postgresql-devel -y

# PostgreSQL Dev Tool Install
pip install psycopg2-binary
# pip install psycopg2

# user switching
# postgres 유저 내 생성되는 Data Directory 접근은 가능하지만 다른 유저에서는 생성하지 못한다.
sudo su - postgres

# # initialize database
# initdb
# pg_ctl -D /var/lib/pgsql/data -l logfile start

# # Database 설정
# # psql 이용 접속 후 나머지 작업은 initial_settings_db.sql 파일 실행
# psql

