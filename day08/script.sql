create database autoever;
use autoever;
create table usertbl (
	userid char(15) not null primary key,
	name varchar(20) not null,
	birthyear int not null,
	addr char(100),
	mobile char(11),
	mdate date
);
commit;
insert into usertbl values('ㄱㄱ', '하니', 1989, '영국', '01000000000', '1977-03-30');
select * from usertbl;


desc usertbl;

-- drop procedure myproc;
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

create table member(
	userid char(15) not null primary key,
	filename varchar(1000),
	filecontent longblob
);

select * from member;