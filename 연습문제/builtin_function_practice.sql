-- 내장함수 : 데이터 아이템 조작의 효율성 증진
-- 문자함수
SELECT LOWER('Hello'), UPPER('Hello');
SELECT CONCAT('Hello', 'World!'); -- 문자열 이어 붙이지
SELECT SUBSTR('Hello World', 3),SUBSTR('Hello World', 3, 3),SUBSTR('Hello World', -3, 3);  -- 문자열 추출
SELECT LENGTH('Hello World'); -- 문자열 길이
SELECT INSTR('Hello World', 'l'); -- 찾을 문자열 위치
SELECT LOCATE('o', 'Hello World', 6); -- 6이후 위치부터 찾을 문자열 위치
SELECT TRIM('  aabb bbaa  '); -- 공백 자르기
SELECT LTRIM('  aabb bbaa  ');
SELECT RTRIM('  aabb bbaa  ');

SELECT REPLACE('010.111.1234','.','-'); -- 문자열 바꾸기

-- 문) 직원테이블에서 이름에 '이'가 포함된 직원이 있다면 '이'부터 두글자만 출력
-- ex) 이순신:이순    참이슬:이
SELECT SUBSTR(jikwon_name, INSTR(jikwon_name,'이'), 2) AS 이포함,jikwon_name  FROM jikwon WHERE jikwon_name LIKE '%이%';


--숫자함수
SELECT ROUND(45.6789,2),ROUND(45.6789),ROUND(45.6789,0),ROUND(45.6789,-1);
SELECT jikwon_no,jikwon_name,ROUND(jikwon_pay*0.025) AS tex FROM jikwon LIMIT 3; --반올림
SELECT TRUNCATE(45.6789,-1),TRUNCATE(45.6789,0),TRUNCATE(45.6789,1); --버림
SELECT MOD(15,2), 15%2, 15 MOD 2; -- 나머지
SELECT GREATEST(15,4,2,7), LEAST(15,4,2,7), POW(2,3), SQRT(9); --가장 큰값, 가장 작은값, 거듭제곱, 루트
SELECT FORMAT(1.234567,1), FORMAT(1.234567,2), FORMAT(1.234567,3);

--날짜함수
SELECT NOW(),SYSDATE(), CURRENT_TIMESTAMP(),CURDATE(), CURDATE()+0; --날짜함수+숫자 -> 일반 숫자로 변환
SELECT ADDDATE('2020-8-1',3),ADDDATE('2020-8-1',-3),SUBDATE('2020-8-1',3),SUBDATE('2020-8-1',-3); -- 날짜(일) 더하기 빼기(윤년 체크o)
SELECT DATE_ADD(NOW(),INTERVAL 1 MINUTE), DATE_ADD(NOW(),INTERVAL 1 HOUR), DATE_ADD(NOW(),INTERVAL 5 DAY), DATE_ADD(NOW(),INTERVAL 1 MONTH);
SELECT DATE_SUB(NOW(), INTERVAL 1 YEAR), DATE_SUB(NOW(), INTERVAL -1 YEAR);
SELECT DATEDIFF(NOW(), '2017-3-1'), TIMEDIFF('23:23:59','12:11:10'); -- 날짜 시간 차이
SELECT LAST_DAY(SYSDATE()), DAYOFYEAR(SYSDATE()), DAYOFWEEK(SYSDATE()),DAYOFMONTH(SYSDATE());

--date_format
SELECT DATE_FORMAT(NOW(),'%Y%m%d'),DATE_FORMAT(NOW(),'%Y-%m-%d'),DATE_FORMAT(NOW(),'%y년%M월%D일');
SELECT DATE_FORMAT(NOW(),'%H%i%s'),DATE_FORMAT(NOW(),'%h시%i분%s초');
SELECT DATE_FORMAT(NOW(),'%d'), DATE_FORMAT(NOW(),'%w'),DATE_FORMAT(NOW(),'%a');
SELECT jikwon_name, jikwon_ibsail, DATE_FORMAT(jikwon_ibsail, '%W') FROM jikwon LIMIT 5;

--형변환 함수
SELECT jikwon_pay*'0.5' FROM jikwon LIMIT 3; --자동 형변환

--문자를 날짜로 변경
SELECT STR_TO_DATE('2020-1-5', '%Y-%m-%d');

--기타함수
-- rank(), (순위 매길려면 정렬을 해야함)
SELECT jikwon_no,jikwon_name,jikwon_pay FROM jikwon ORDER BY jikwon_pay DESC;
SELECT jikwon_no,jikwon_name,jikwon_pay, rank() over(order by jikwon_pay) FROM jikwon;
SELECT jikwon_no,jikwon_name,jikwon_pay, dense_rank() over(order by jikwon_pay DESC) FROM jikwon; --동점자 처리

