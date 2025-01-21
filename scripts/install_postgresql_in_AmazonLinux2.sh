# Amazon Linux 2 - PostgreSQL v.13 install
# Postgresql Insatll
sudo amazon-linux-extras install epel -y
sudo tee /etc/yum.repos.d/pgdg.repo<<EOF
[pgdg13]
name=PostgreSQL 13 for RHEL/CentOS 7 - x86_64
baseurl=http://download.postgresql.org/pub/repos/yum/13/redhat/rhel-7-x86_64
enabled=1
gpgcheck=0
EOF
sudo yum install postgresql13 postgresql13-server

# PostgreSQL Dev Tool Install
pip install psycopg2-binary
pip install psycopg2

# 데이터베이스 설정
sudo /usr/pgsql-13/bin/postgresql-13-setup initdb

# systemctl enable 설정
sudo systemctl enable --now postgresql-13

# 설치한 postgresql 확인
systemctl status postgresql-13

su - postgres

# PostgreSQL Dev Tool Install
pip install psycopg2-binary
pip install psycopg2