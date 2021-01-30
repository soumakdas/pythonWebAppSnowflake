create table colors(color_uid numeric, color_name varchar)

--drop table colors
select * from colors
create or replace sequence color_uid_seq start = 1002 increment = 1;
create or replace sequence color_uid_seq start = 1 increment = 1;

insert into colors values(color_uid_seq.nextval,'Red');
insert into colors values(color_uid_seq.nextval,'Orange');
insert into colors values(color_uid_seq.nextval,'Yellow');
insert into colors values(color_uid_seq.nextval,'Green');
insert into colors values(color_uid_seq.nextval,'Blue');
insert into colors values(color_uid_seq.nextval,'Indigo');
insert into colors values(color_uid_seq.nextval,'Violet');


select color_name, count(*)
from colors group by color_name;



update colors set color_name = 'Das'
where color_name = 'Indigo'