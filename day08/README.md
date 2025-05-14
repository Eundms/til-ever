# 파이썬과 데이터베이스 연동
## 0. 준비 
- 사용할 데이터베이스 서버를 확인 : MariaDB, MongoDB 모두 구동되어 있는지 확인 

## 1. 데이터베이스 연동 방법
1) 프로그래밍 언어에 드라이버를 설치해서 직접 연동하는 방식
- ex) pymongo 
- 드라이버가 필요한 이유 : 인터페이스 + 드라이버 

2) 프레임워크를 이용하는 방식
- SQL Mapper를 이용하는 방식 : RDBMS에서 가능
    - ex) MyBatis 
- ORM 형태를 이용하는 방식 : RDBMS의 테이블을 프로그래밍 언어의 Class와 매핑하고 데이터를 Instance와 매핑하는 방식의 프레임워크 
    - Hibernate(Java)
    - SQLAlchemy(Django)

## 2. 데이터베이스 연동 
### mongodb 
- pip install pymongo

### mariadb 
- pip install pyMySQL

```python
import pymysql
변수 = pymysql.connect(host = '데이터베이스 위치', port= '포트번호', user = '계정', passwd= '비밀번호', db = '데이터베이스이름', charset = '인코딩방식')
```

## 3. DML 수행
1. 과정 : 연결 객체의 cursor 메서드를 호출해서 sql 실행 객체를 가져옵니다
2. sql 실행 객체.execute(sql 문장)
   - 연결 객체에서 commit()을 호출하면 반영되고 rollback()을 호출하면 취소 

- PreparedStatement 권장 

## 조회 
- 조회 함수는 fetchone과 fetchall
- fetchone은 하나의 데이터를 조회하는 함수이고 fetchall은 0개 이상의 데이터를 조회하는 함수
- 함수를 호출하면 결과 집합을 리턴하게 되는데 fetchone은 tuple을 리턴하고 fetchall은 tuple의 tuple을 리턴 


- `tuple` : 데이터 수정 불가능 + 행 

## 프로시저
- 관계형 데이터베이스 사용하는 절차적 프로그래밍을 위한 개체
  - 사용하는 이유 
    - 보안 : 개발자에게 `데이터베이스 구조를 알려주지 않고 DML 작업이 가능하도록` 한다 
    - 속도 : `Procedure, View` 는 한번 불러들이면 `메인 메모리에 캐싱된 상태`로 쓰이기 때문에 `실행 속도가 빠르다`
- 프로시저는 `스크립트로 실행`한다

```sql
DROP PROCEDURE IF EXISTS myproc;
DELIMITER //

CREATE PROCEDURE myproc(
	vuserid CHAR(15), 
	vname VARCHAR(20), 
	vbirthyear INT,
	vaddr CHAR(100),
	vmobile CHAR(11),
	vmdate DATE
)
BEGIN
	INSERT INTO usertbl(userid, name, birthYear, addr, mobile, mDate)
	VALUES(vuserid, vname, vbirthyear, vaddr, vmobile, vmdate);
END //

DELIMITER ;

CALL myproc('2eee', '권보아', 1986, '남양주', '01012345678', '1986-11-05');

select * from usertbl;
```

## 파이썬에서 프로시저 호출
  - `cursor객체.callproc(프로시저이름, args = (매개변수나열))`

## BLOB 데이터 연동
- Binary Large Object의 약자로 바이너리 코드를 저장하는 자료형 
- 그림, 오디오 등의 멀티미디어 데이터를 원본을 저장할 때 사용 

## 파일 데이터를 저장하는 방법
1. 파일의 경로를 저장하는 방식 : 파일 시스템 변경에 따른 영향이 있음
2. 파일의 원본 데이터를 저장하는 방식 
- open으로 파일을 읽는다 