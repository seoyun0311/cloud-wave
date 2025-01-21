---데이터 베이스 생성 / 계정 생성 / 권한 할당 / 데이터베이스 소유자 변경
create database trip_advisor;
create user "user" with password 'qwer1234';
grant all privileges on database trip_advisor to "user";
alter database trip_advisor owner to "user";