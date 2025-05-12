# DML (데이터 조작 언어)
- 이론에서는 SELECT, INSERT, DELETE, UPDATE 4가지를 DML로 보지만 실무에서는 SELECT을 DQL(Data Query Language)로 구분합니다.  

## CQRS 
- 조회 MongoDB(NoSQL), 삽입,삭제,수정(RDBMS)

## Insert
- `insert into tCity(name, area, popu, metro, region) values ('쥬니', 50, 100, 'n', '경기');`
- `desc 테이블명`
### 구조 동일한 테이블 작성 :  WHERE 절에 거짓인 조건을 기술하기 
- `select * from emp where 0=1;`

### 여러 insert 구문에서 에러 발생시에도 다음 스크립트 실행하기 
- 여러 개의 insert 구문을 수행할 때 insert와 into 사이에 ignore을 추가하면 에러가 발생하더라도 다음 스크립트를 실행한다 

# 자동으로 커밋되는 SQL 명령어
- DDL (Data Definition Language) 명령어
- DCL (Data Control Language) 명령어 
- TCL (Transaction Control Language) 명령어

## Update
```sql
create table deptcopy as select * from tStaff2;
select * from deptcopy;
select * from deptcopy;
update deptcopy set popu = 100, region = '충청' where name = '오산';
	

update dept set loc  = (
	select loc from dept where deptno = 40
) 
where deptno = 20;
```

## Delete
```sql
delete from emp where deptno = (select deptno from dept where dname = 'SALES');
```