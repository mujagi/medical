create table daum_movie(
DNO number,
title varchar2(300),
img varchar2(300),
audience varchar2(300),
ddate date
);

drop table daum_movie;
select *from daum_movie;


create table coupang(
cno number,
title varchar2(100),
img  varchar2(100),
price number(10),
grade number(10),
eval_num number(10)
);

create table flight(
fno number(4),
airline varchar2(100),
departure_time date,
arrival_time date,
flight_time varchar2(20),
price number(10)
);