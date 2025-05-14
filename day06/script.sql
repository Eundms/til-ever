create table tCityDefault(
	name char(10) primary key,
	area int null,
	popu int null,
	metra char(1) default 'n' not null,
	region char(6) not null
);


insert into tCityDefault values('k', 1, 1, default, 'seoul');
insert into tCityDefault(name, area, popu, region)
values('1', 1, 1,'seoul');

select * from tCityDefault;


# 테이블의 모든 데이터 삭제
truncate table tCityDefault;

desc tCityDefault;
ALTER TABLE tCityDefault
CHANGE COLUMN metra metro char(1);

insert into tCityDefault(name, area, popu, metro, region) values
('오산', 42, 21, 'n', '경기'),
('ㅇ', 432, 21, 'n', '오산'),
('ㄹ', 412, 21, 'n', '충청'),
('ㅁ', 2, 3, 'n', '전라');

create table tStaff(
	name char(10) primary key,
	salary int null,
	score int null,
	joindate char(10),
	grade char(10),
	gender char(1) default 'n' not null,
	depart char(6) not null
);

insert into tStaff(name, depart, gender, joindate, grade, salary, score)
select name, region, metro, '20110505', '신입', area, popu
from tCityDefault
where region ='경기';


create table tStaff2 as
select name, region, metro, '20110505', '신입', area, popu
from tCityDefault
where region ='경기';

desc tStaff2;

select * from tStaff2;
delete from tStaff2 where name = 'a';

-- 특정 시점으로 돌아가기
insert into dept values(70, '비서', '파주');
savepoint s1;
insert into dept values(80, '비서', '포천');
select * from dept;
rollback to s1;
select * from dept;