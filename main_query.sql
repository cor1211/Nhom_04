Create database if not exists StudentManagement
Use StudentManagement
Create table if not exists Student(
	student_id char(10) primary key,
    student_name varchar(50) not null,
    student_birth date not null,
    student_address varchar(150),
    student_cccd char(12) unique,
    student_phone varchar(20),
    student_email varchar(100) unique,
    student_gender enum ('Nam','Nữ','Khác'),
    student_generation varchar(10),
    student_image varchar(500),
    class_id int not null,
    major_id int not null,
    foreign key (major_id) references Major(major_id)
    on delete cascade
    on update cascade,
    foreign key (class_id) references Class(class_id)
    on delete cascade
    on update cascade
    
)

select * from student
drop table student

insert into Student 
values
('2022602800','Lưu Công Vinh','2004-11-12','Hà Nội','001204056492','0348341246','vinh01@gmail.com','Nam','K17','D:/học/Tài Liệu CNTT/Student Management/static/images/Luu Cong Vinh.jpg',2,1),
('2022602801','Nguyễn Anh Quân','2004-04-25','Hà Nội','001204056493','0348341247','vinh02@gmail.com','Nữ','K17',"D:/học/Tài Liệu CNTT/Student Management/static/images/241513085_1029049977913764_3198139055762524429_n.jpg",5,3),
('2022602802','Nguyễn Anh Lạc','2000-04-25','Hà Nội','001204056494','0348341248','vinh03@gmail.com','Khác','K15',"D:/học/Tài Liệu CNTT/Student Management/static/images/Xayah (AI-Generated)_ Credit_ namakxin.jpg",8,4)
;
drop table Department
Create table if not exists Department(
department_id int auto_increment primary key,
department_name varchar(100) not null
)
select * from Department
insert into Department (department_name)
values
('Công nghệ thông tin'),
('Kinh tế');

create table if not exists Major(
major_id int auto_increment primary key,
major_name varchar(100) not null,
department_id int not null,
foreign key (department_id) references Department(department_id)
On delete cascade
on update cascade
);

insert into Major(major_name, department_id)
values
('Công nghệ thông tin',1),
('Kĩ thuật phần mềm',1),
('Kinh tế quốc tế',2),
('Kinh doanh quốc tế',2)

drop table Major
select * from Major

Create table if not exists Class
(
	class_id int auto_increment primary key,
    class_name varchar(100) not null,
    major_id int not null,
    department_id int not null,
    foreign key (major_id) references Major(major_id)
    On delete cascade
    On update cascade,
    foreign key (department_id) references Department(department_id)
    On delete cascade
    On update cascade
);

insert into Class (class_name, major_id, department_id)
values
('2022CNTT01',1,1),
('2022CNTT02',1,1),
('2022KTPM01',2,1),
('2022KTPM02',2,1),
('2022KTQT01',3,2),
('2022KTQT02',3,2),
('2022KDQT01',4,2),
('2022KDQT02',4,2)
Truncate table Class
select * from class

select Class.class_id,
    Class.class_name,
    Major.major_id,
    Major.major_name,
    Department.department_id,
    Department.department_name
From Class
Join Major
On Major.major_id = Class.major_id
JOIn Department
On Department.department_id = Major.department_id;

select Student.*, Class.class_name, Major.major_name, Department.department_name
FROM Student
JOIN Class
On Student.class_id = Class.class_id
Join Major 
On Student.major_id = Major.major_id
Join Department
On Major.department_id = Department.department_id

create table if not exists Subject(
subject_id char(10)  primary key,
subject_name varchar(100) not null ,
subject_credit int not null
);

insert into Subject()
values
('PE6021','Bóng  rổ', 1),
('FL6085','Tiếng anh CNTT cơ bản 1',5),
('BS6002','Giải tích',3),
('LP6010','Triết học Mác-Lênin',3),
('BM6091','Quản lý dự án',2)


select * from subject

drop table Subject

create table if not exists Subject_Student(
subject_id char(10) not null,
student_id char(10) not null,
ss_semester varchar(50) not null,
score_regular float,
score_midterm float,
score_final float,
primary key (subject_id, student_id, ss_semester),
foreign key (subject_id) references Subject(subject_id)
on delete cascade
on update cascade,
foreign key (student_id) references Student(student_id)
on delete cascade
on update cascade 
);
select * from Subject_Student
drop table Subject_Student

insert into Subject_Student()
values
('BM6091','2022602800','HK1',8.5,9,10),
('BS6002','2022602800','HK1',8,9.5,10),
('FL6085','2022602800','HK1',9,9.5,10),
('LP6010','2022602800','HK2',8.5,9.5,10),
('BM6091','2022602801','HK1',8,9.5,10),
('BS6002','2022602801','HK1',8.5,9.5,4),
('FL6085','2022602801','HK2',9,9,5.5),
('LP6010','2022602801','HK2',8,9.5,10),
('LP6010','2022602802','HK2',7,9.5,10),
('BS6002','2022602802','HK2',8.5,8,8),
('FL6085','2022602802','HK3',9,9.5,9),
('LP6010','2022602802','HK4',8,9,7);

select subject_student.*, subject.subject_credit from subject_student
join subject on subject.subject_id = subject_student.subject_id

select student.student_id,student.student_name,
      sum(
      Case
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 8.5 then 4
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 8 then 3.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 7 then 3
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 6.5 then 2.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 5.5 then 2
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 5 then 1.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 4 then 1
      else 0
      end *subject.subject_credit)/sum(subject.subject_credit) as gpa
      from Student
      left join subject_student on subject_student.student_id = student.student_id
      left join subject on subject.subject_id = subject_student.subject_id
      group by student.student_id
      
select student.student_id, subject_student.*,subject.*
from Student
left join subject_student on subject_student.student_id = student.student_id
left join subject on subject.subject_id = subject_student.subject_id


Select Student.student_id,Student.student_name, 
      Student.student_gender,Student.student_birth, 
      Student.student_generation, Major.major_name, 
      Class.class_name,
      sum(
       Case
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 8.5 then 4
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 8 then 3.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 7 then 3
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 6.5 then 2.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 5.5 then 2
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 5 then 1.5
      When subject_student.score_regular*0.2 + subject_student.score_midterm *0.3+subject_student.score_final*0.5 >= 4 then 1
      else 0
      end * subject.subject_credit)/sum(subject.subject_credit) as gpa
      from Student
      Join Major on Student.major_id = Major.major_id
      Join Class on Student.class_id = Class.class_id
      LEFT JOIN SUBJECT_STUDENT ON SUBJECT_STUDENT.student_id = Student.student_id
      LEFT JOIN SUBJECT ON SUBJECT.subject_id = Subject_Student.Subject_id
      Group by Student.student_id
