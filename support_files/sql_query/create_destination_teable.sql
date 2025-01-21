---trip_advisor 데이터베이스 접속
---Command: psql -U user -d trip_advisor

---테이블 생성
CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    average_rating VARCHAR(10),
    photo_url VARCHAR(255)
);

---테스트 데이터 입력
INSERT INTO attractions (name, location, average_rating, photo_url) VALUES 
('Eiffel Tower', 'Paris, France', 4.7, 'https://lh5.googleusercontent.com/p/AF1QipOnJHzIOu1VUvkTX0GKjmqK-NdgXWJEUa8m2YPd=w540-h312-n-k-no'),
('Great Wall of China', 'Beijing, China', 4.8, 'https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcSNsVSfi_LRcKaaxzjCs-Aq1_9YS7WAN7d4rrC_Oecn5n0D3Jkm8klHCLU6Eo9cZNRctYeEuTL_3jL_xUATWJOuSJm62z54'),
('Statue of Liberty', 'New York, USA', 4.6, 'https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcQeve9KWo7zk7gXpRgaBDhfeCklifCZqaLWPXXJgKJJCFpYSp7kauVOlyt1nmNLi9UqT9P4SiUFBLihf5omTv-bdR8LLTWv'),
('Taj Mahal', 'Agra, India', 4.9, 'https://lh3.googleusercontent.com/p/AF1QipOIwFX7pMJXtOZ5zEkes4rLws69dgeTYas5C1p4=s680-w680-h510'),
('Colosseum', 'Rome, Italy', 4.8, 'https://lh3.googleusercontent.com/p/AF1QipNtY2FidGEO7yj8kqm-h-ixL3H27DmKOD8dAwvK=s1360-w1360-h1020'),
('Machu Picchu', 'Cusco Region, Peru', 4.9, 'https://lh3.googleusercontent.com/p/AF1QipOHVkYSLcE9rOozPl9UPtEz4ga0IkMVD5_4J-NM=s1360-w1360-h1020'),
('Gyeongbokgung Palace', 'Seoul, South Korea', 4.7, 'https://lh3.googleusercontent.com/p/AF1QipPe2q2PPeip1zVjV6UI4FHCkdFxIglodID7c0a3=s1360-w1360-h1020'),
('Sydney Opera House', 'Sydney, Australia', 4.7, 'https://lh3.googleusercontent.com/p/AF1QipMHftgSCBlvyjxYphi4gLqDC_62WWvZvyy1EBuh=s1360-w1360-h1020'),
('Waikiki Beach', 'Honolulu, Hawaii', 4.5, 'https://www.vmcdn.ca/f/files/glaciermedia/import/lmp-all/1621129-hawaiian-islands-jpg-w-960.jpg');

---내용 수정 코드
UPDATE attractions 
SET photo_url = 'https://newexample.com/newpyramidsofgiza.jpg'
WHERE name = 'Pyramids of Giza';
