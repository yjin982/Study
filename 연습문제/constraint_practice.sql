-- 문제
-- 제약조건 연습
CREATE TABLE professor(
	pro_code INT PRIMARY KEY, 
	pro_name CHAR(10), 
	lab INT CHECK(lab >= 100 AND lab <= 500)
)CHARSET=UTF8;
CREATE TABLE subject(
	sub_code INT PRIMARY KEY AUTO_INCREMENT, 
	sub_name CHAR(20) UNIQUE, 
	sub_book CHAR(20), 
	pro_code INT, 
	FOREIGN KEY(pro_code) REFERENCES professor(pro_code)
)CHARSET=UTF8;
CREATE TABLE student(
	std_code INT PRIMARY KEY, 
	std_name CHAR(10), 
	sub_code INT, 
	grade INT CHECK (grade IN(1,2,3,4)), 
	FOREIGN KEY(sub_code) REFERENCES subject(sub_code)
)CHARSET=UTF8;
ALTER TABLE student ALTER COLUMN grade SET DEFAULT 1;

--제약조건 확인
SELECT * FROM information_schema.table_constraints WHERE TABLE_NAME='professor';
SELECT * FROM information_schema.table_constraints WHERE TABLE_NAME='subject';
SELECT * FROM information_schema.table_constraints WHERE TABLE_NAME='student';

-- 교수   교수코드:pk / 교수명 / 연구실:100~500
-- 과목   과목코드:pk, 1부터 1씩 자동증가 / 과목명:유니크 / 교재명 / 담당교수:fk[교수-교수코드] 
-- 학생   학번:pk / 학생명 / 수강과목:fk[과목-과목코드] / 학년:1~4학년만,초기치 1
SELECT * FROM professor;
INSERT INTO professor VALUES(1, '김교수', '100');
INSERT INTO professor VALUES(2, '박교수', '500');
--INSERT INTO professor VALUES(3, '최교수', '99'); --연구실 확인
--INSERT INTO professor VALUES(3, '최교수', '555'); --연구실 확인

SELECT * FROM subject;
INSERT INTO subject VALUES(1,'DB', 'DB의 모든것', 1);
INSERT INTO subject VALUES(0, '자바', '자바커피', 2); -- 과목코드 자동증가
INSERT INTO subject VALUES(0, 'C언어', 'hello World', 2); -- 과목코드 자동증가
--INSERT INTO subject VALUES(4, 'C언어', '씨언어다', 2); -- 유니크 확인


SELECT * FROM student;
INSERT INTO student VALUES(1, '김가연', 1, 1);
INSERT INTO student VALUES(2, '최민수', 1,DEFAULT); --default 확인
INSERT INTO student VALUES(3, '박영희', 2, 4);
INSERT INTO student VALUES(4, '홍홍홍', 3, 3);
-- INSERT INTO student VALUES(4, '홍홍홍', 3, 5); --학년 제한