---trip_advisor 데이터베이스 접속
---Command: psql -U user -d trip_advisor

---데이터 생성
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, email, password) 
VALUES ('user', 'user@admin.abc', 'qwer1234');