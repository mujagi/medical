-- 2개 테이블 : department_id

select *from emoloyees;

select *from departments;

select employee_id,emp_name,a.department_id,department_name
from employees a,departments b
where a.department_id = b.department_id
;

select *from stu_score;

select *from students;

alter table students add no number(38);

insert into students(no) select no from stu_score
;
insert into students(ID,name) values(
'aaa',
);


-- rownum 만들어진 번호를 no 넣기
update students b set no = 
(select rnum from (select rownum rnum,id from students a))
where a.id = b.id;

update students b
set no = a.rnum
from 
(select rownum rnum,id from students) a
where b.id = a.id;
-- 홍길동
-- 학생성적의 모든내용과 전화번호,이메일,과,학년

select no,name,kor,eng,math,total,avg,rank,c_date from stu_score
where name = '홍길동';

select id,name, phone,email,major,grade from students
where name = '홍길동';

select no,a.name,phone,email,major,grade,kor,eng,math,total,avg,rank,c_date 
from stu_score a, students b
where a.name = '홍길동' and a.name=b.name;


select *from stu_score
order by no;

select count(*) from stu_score;

select count(*) from students;

drop table students;

-- equi join
-- 2개 테이블 join - 1개의 동일한 컬럼 있어야함.
-- 동일한 컬럼은 중복이 없어야 함. 2개중 하나의 테이블 에서는 primary키가 사용이 되어야함.

select a.id,a.name,phone,total,avg from students a,stu_score b
where a.id = b.id
;

-- self join
-- 동일한  테이블 2개를 가지고 서로 join
select employee_id, department_id,manager_id,job_id from employees
order by department_id;

desc stu_score;

desc students;

drop table students;

select *from students;

select *from stu_score;

update stu_score a
set rank = (select ranks from (select no,id,rank() over(order by total desc) as ranks ,rank,total from stu_score)b
where a.no = b.no)
;

select *from students;

select *from member;

alter table member add no number;

select*from member;

-- rank, id
select rownum, id from member;

--rnum
select rnum from(select rownum rnum, id from member)b
where id=b.id;

update member a
set no = ( select rnum from(select rownum rnum, id from member)b
where a.id=b.id);

update stu_score set rank = 0 ;

commit;

select total,rank from stu_score
order by total desc;

--
select total,rank() over (order by total desc) ranks from stu_score;
select row_number() over (order by total desc) rnum,total from stu_score;

-- stuscore, rank 순위를 업데이트 하세요.



-- 업데이트 하는 방법
update stu_score a set rank = (
select ranks from (select no,rank() over (order by total desc) ranks from stu_score)b
where a.no = b.no)
;

select *from stu_score;


-- row number() over()

select *from stu_score;


--
select *from 
(select rownum rnum, a.* from 
(select *from stu_score order by total desc)a)
where rnum >= 1 and rnum<=20 
;

select *from(
select row_number() over(order by total desc) rnum, a.* from stu_score a)
where rnum >= 1 and rnum <= 10
;

select employee_id,emp_name,manager_id from employees
order by employee_id
;

--self join manager_id, 이름 출력하시오
-- 값이 충족되지 않아도 출력되도록 하는것
-- null 값이 있는 반대편 항목에 (+)기호를 넣으면 됨.
select a.employee_id,a.emp_name,a.manager_id,b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id(+);

select *from employees;

select manager_id, emp_name from employees
where emp_name = 'Diana Lorentz';

-- equi join ,outer join employees 테이블 부서번호 10~110
select emp_name,a.department_id,department_name 
from employees a, departments b 
where a.department_id(+) = b.department_id
order by department_id
;

-- 부서번호 10~270
select department_id from departments ;

 --ansi join
select *from employees cross join departments;
select *from employees,departments;

select a.department_id,department_name 
from employees a, departments b
where a.department_id = b.department_id
;

-- ansi inner join - using
select employee_id,emp_name,department_id,department_name
from employees  join departments 
using (department_id)
;

select a.*,department_name
from employees a, departments b
where a.department_id = b.department_id
;

-- natural join
select department_id, department_name 
from employees  natural join departments ;

-- ansi outer join - left outer join,right outer join,fullouter join
select a.manager_id,b.emp_name
from employees a
left outer join employees b
on a.manager_id = b.employee_id;

-- 기본 sql left outer join.right outer join, full outer join은 불가
select a.emp_name,a.manager_id,b.emp_name
from employees a ,employees b
where a.manager_id = b.employee_id;


