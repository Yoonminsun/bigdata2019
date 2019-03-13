describe basic_student_info;
describe student_language;
select * from basic_student_info;
select * from student_language;
-- Equi Join (=)
SELECT * FROM basic_student_info b, student_language s 
where b.Student_ID = s.Student_ID;
-- Inner Join (테이블의 ON 절의 조건이 일치하는 결과만 출력)
SELECT * FROM basic_student_info b INNER JOIN student_language s 
ON b.Student_ID = s.Student_ID;
-- Join with USING (USING 절에 참조할 데이터를 넣고, 중복 되지 않게 함)
SELECT * FROM basic_student_info b JOIN student_language s USING(Student_ID);
-- Outer Join _ Left Join 
-- (왼쪽 테이블은 무조건 가져오고 오른쪽과 매칭되지 않는 부분은 NULL)
-- ON 대신 USING을 사용하여 참조데이터를 지정하고, 중복을 방지함
-- ORDER BY 를 이용하여 Student_ID를 기준으로 정렬
SELECT * FROM basic_student_info b LEFT JOIN student_language s
USING(Student_ID) ORDER BY Student_ID;