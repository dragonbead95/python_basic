BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER primary key,             username text, email text,             phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kim','Kim@naver.com','010-1234-5678','Kim.com','2020-08-24 17:35:10');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-1111-1111','Park.com','2020-08-24 17:35:10');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2020-08-24 17:35:10');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-3333-3333','Cho.com','2020-08-24 17:35:10');
INSERT INTO "users" VALUES(5,'Yoo','You@naver.com','010-4444-4444','Yoo.com','2020-08-24 17:35:10');
COMMIT;
