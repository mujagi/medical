-- 2�� ���̺� : department_id

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


-- rownum ������� ��ȣ�� no �ֱ�
update students b set no = 
(select rnum from (select rownum rnum,id from students a))
where a.id = b.id;

update students b
set no = a.rnum
from 
(select rownum rnum,id from students) a
where b.id = a.id;
-- ȫ�浿
-- �л������� ��系��� ��ȭ��ȣ,�̸���,��,�г�

select no,name,kor,eng,math,total,avg,rank,c_date from stu_score
where name = 'ȫ�浿';

select id,name, phone,email,major,grade from students
where name = 'ȫ�浿';

select no,a.name,phone,email,major,grade,kor,eng,math,total,avg,rank,c_date 
from stu_score a, students b
where a.name = 'ȫ�浿' and a.name=b.name;


select *from stu_score
order by no;

select count(*) from stu_score;

select count(*) from students;

drop table students;

-- equi join
-- 2�� ���̺� join - 1���� ������ �÷� �־����.
-- ������ �÷��� �ߺ��� ����� ��. 2���� �ϳ��� ���̺� ������ primaryŰ�� ����� �Ǿ����.

select a.id,a.name,phone,total,avg from students a,stu_score b
where a.id = b.id
;

-- self join
-- ������  ���̺� 2���� ������ ���� join
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

-- stuscore, rank ������ ������Ʈ �ϼ���.



-- ������Ʈ �ϴ� ���
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

--self join manager_id, �̸� ����Ͻÿ�
-- ���� �������� �ʾƵ� ��µǵ��� �ϴ°�
-- null ���� �ִ� �ݴ��� �׸� (+)��ȣ�� ������ ��.
select a.employee_id,a.emp_name,a.manager_id,b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id(+);

select *from employees;

select manager_id, emp_name from employees
where emp_name = 'Diana Lorentz';

-- equi join ,outer join employees ���̺� �μ���ȣ 10~110
select emp_name,a.department_id,department_name 
from employees a, departments b 
where a.department_id(+) = b.department_id
order by department_id
;

-- �μ���ȣ 10~270
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

-- �⺻ sql left outer join.right outer join, full outer join�� �Ұ�
select a.emp_name,a.manager_id,b.emp_name
from employees a ,employees b
where a.manager_id = b.employee_id;


