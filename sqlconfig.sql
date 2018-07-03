insert into mysql.user(Host,User,Password) values("localhost","flask",password("1611102"));
create database c2cweb;
grant all privileges on c2cweb.* to flask@localhost identified by '1611102';flush privileges;
