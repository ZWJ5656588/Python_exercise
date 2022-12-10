-- 1.表结构

create table tb_teacher
(
    id      int unsigned primary key auto_increment not null,
    -- varchar自动补0
    name    varchar(50) not null,
    tel     char(11)    not null unique,
    -- boolean 类型在sql中保存为tinyint(1)
    married  boolean    not null default false
);

-- 2.添加表结构
alter table tb_teacher add sal decimal(5,2) not null;
-- decimal(5,2) 表示整数位位，小数位2位

-- 3.修改表结构
alter table tb_teacher change sal salary  decimal(7,2) not null;
alter table tb_teacher add school varchar(20) not null ;

-- 4.插入数据
insert into tb_teacher values (0,'朱文峻','19130616725',0,35000.13);
insert into tb_teacher values (0,'张三','15296',1,15234.236,'电子科技大学');


--5.修改数据
update tb_teacher set salary=35000.13 where id=1;
update tb_teacher set school='西南交通大学' where  id=1;
update tb_teacher set tel='15828262997' where id=2;

--6. 查询数据，字段可跟表达式，可以重命名
-- salary *12 的年收入用income表示
select name,tel,salary*12 as income from tb_teacher;

/* 注意，from 子句句的优先级大于select字句，所以先执行from子句
 */

--7. 数据表的分页
select id as 序号 ,salary*12 as income from tb_teacher limit 0,2;

-- 8. 聚合函数
select sum(salary*12)/count(*) as avg_income from tb_teacher;

-- 注意，聚合函数不能出现在where中,因为聚合函数针对结果集,而where在结果集之前运行
-- 要查询students表中超过平均身高的人数，如何进行？
-- 可以使用子查询
select * from students where  height> (select avg(height) from students) order by height desc ;

-- 9.group by +group concat(分组集合显示)
select gender as 性别 , group_concat(name) as 姓名 from students group by  gender;
/* 注意，分组条件后面跟,再加分组集合
 */

select gender,group_concat(height) from students group by gender;

select gender as 性别, count(*) as 人数 from students group by gender;

/*1. having 条件表达式：用来分组查询后指定一些条件来输出查询结果
2. having作用和where一样，但having只能用于group by
*/

-- 分组聚合
select gender as 性别 ,round(avg(height)) as 平均身高   --round 函数将小数四舍五入变成整数
from students group by gender having 平均身高>160.00;

-- 10. 排序
select * from students order by height desc;  -- 倒叙
select * from students order by  height desc,age;  --身高降序，身高一样时年龄升序
/* 注意，分页limit 的顺序在最后*/

-- 11. distinct 去重
/* distinct 只能执行一个字段*/

-- 12. 查询10部门中收入超过150000且工龄超过20年的员工信息
select emnpo,ename,salary,hiredate
from t_temp
where deptno=10
and(sal+isfull(comm,0))*12>=150000
and datediff(now(),hiredate)/365>=20;

--ifnull(expr1.expr2):isfull函数，当地一个参数值为null，返回第二个参数值
--datediff(expr1,expr2):datediff函数，返回第1个时间与2个时间的日期差值，如果时间精确到时分秒，只取日期部分
SELECT DATEDIFF('2007-12-31 23:59:59','2007-12-30');

SELECT DATEDIFF('2010-11-30 23:59:59','2010-12-31');

-- 范围运算符in
--查询10,20,30,部门里1985以前入职的，而且不能是'salesman'职位的员工
select empno,ename,sal,deptno,hiredate
from t_emp
where deptno in (10,20,30)
and job!='salesman' and hiredate<'1985-01-01'

--13.分组查询进阶
select gender,group_concat(name) as  姓名,max(height),min(height),avg(height),count(*)
from students where height>175.00 group by gender;

/* sql子句的执行顺序 from>where > group by > having > select > order by > limit
 */

-- 14.表的关联
-- 小心count(*)也会统计null
select classes.name,count(*) from students left join classes
on students.cls_id=classes.id group by classes.name;

select students.cls_id,count(*) from students left join classes
on students.cls_id=classes.id group by students.cls_id;

-- 查询各班级中的人数，不显示错误班级
select students.cls_id,count(classes.id) from students left join classes
on students.cls_id=classes.id group by students.cls_id;

