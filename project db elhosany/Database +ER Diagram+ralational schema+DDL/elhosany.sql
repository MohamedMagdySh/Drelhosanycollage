CREATE TABLE students (
student_id INT PRIMARY KEY ,
fname VARCHAR(10) NOT NULL,
mname VARCHAR(10) NOT NULL,
lname VARCHAR(10) NOT NULL,
data_birth DATE,
yearenrrow YEAR NOT NULL,
address VARCHAR(30),
collage_name VARCHAR(30),
prog_id INT
);

CREATE TABLE program (
program_id INT PRIMARY KEY,
program_name TEXT NOT NULL,
manage_program TEXT NOT NULL,
start_date YEAR NOT NULL
);

CREATE TABLE instractor (
instractor_id INT PRIMARY KEY,
name_instractor TEXT NOT NULL,
age INT,
salary DOUBLE NOT NULL,
prog_id INT
);

CREATE TABLE courses (
courses_id INT PRIMARY KEY,
courses_name TEXT NOT NULL,
point_courses INT NOT NULL,
prog_id INT
);

CREATE TABLE takes (
stud_id INT ,
cour_id INT ,
year_course YEAR,
semster VARCHAR(10) CHECK (semster IN ('first','second','summer')),
mark DOUBLE CHECK (mark<100 AND mark>0),
grade VARCHAR(2),
PRIMARY KEY(stud_id,cour_id)
);

CREATE TABLE gives (
instr_id INT ,
cour_id INT ,
PRIMARY KEY(instr_id,cour_id)
);
/*-------------------------------------------------------------------------------------------*/
ALTER TABLE students ADD CONSTRAINT FOREIGN KEY (prog_id) REFERENCES program (program_id);
ALTER TABLE courses ADD CONSTRAINT FOREIGN KEY (prog_id) REFERENCES program (program_id);
ALTER TABLE instractor ADD CONSTRAINT FOREIGN KEY (prog_id) REFERENCES program (program_id);
ALTER TABLE gives ADD CONSTRAINT FOREIGN KEY (instr_id) REFERENCES instractor (instractor_id) ;
ALTER TABLE gives ADD CONSTRAINT FOREIGN KEY (cour_id) REFERENCES courses (courses_id) ;
ALTER TABLE takes ADD CONSTRAINT FOREIGN KEY (stud_id) REFERENCES students (student_id) ;
ALTER TABLE takes ADD CONSTRAINT FOREIGN KEY (cour_id) REFERENCES courses (courses_id) ;
/*-------------------------------------------------------------------------------------------*/
INSERT INTO program VALUES(100,'computer science','Elhossiny','2000');
INSERT INTO program VALUES(101,'cyper security','gaafer','2005');
INSERT INTO program VALUES(102,'network','abaas','2009');
INSERT INTO program VALUES(103,'math','shomaan','2015');
/*-------------------------------------------------------------------------------------------*/
INSERT INTO courses VALUES(1000,'Database',3,100);
INSERT INTO courses VALUES(1001,'algorithm',3,100);
INSERT INTO courses VALUES(1002,'vlse',2,102);
INSERT INTO courses VALUES(1003,'mecanica',4,103);
INSERT INTO courses VALUES(1004,'logic',1,101);
INSERT INTO courses VALUES(1005,'embedded',3,100);
/*-------------------------------------------------------------------------------------------*/
INSERT INTO students VALUES(1,'mohamed','magdy','shaban','2004-5-15',2022,'menofia, sadat city','electronic engineer',100);
INSERT INTO students VALUES(2, 'ahmed', 'ali', 'hassan', '2003-8-20', 2021, 'cairo, nasr city', 'electronic engineer', 100);
INSERT INTO students VALUES(3, 'sara', 'mohamed', 'farid', '2005-3-12', 2023, 'alexandria, smouha', 'electronic engineer', 102);
INSERT INTO students VALUES(4, 'laila', 'tamer', 'osman', '2004-11-30', 2022, 'giza, dokki', 'faculty science', 103);
INSERT INTO students VALUES(5, 'khaled', 'youssef', 'ali', '2002-6-18', 2020, 'aswan, new aswan city', 'compuer science', 101);
INSERT INTO students VALUES(6, 'nour', 'samy', 'kamel', '2003-1-25', 2021, 'luxor, karanak', 'compuer science', 102);
/*-------------------------------------------------------------------------------------------*/
INSERT INTO takes VALUES(1,1000,2024,'first',99,'A+');
INSERT INTO takes VALUES(1, 1001, 2023, 'second', 95, 'A');
INSERT INTO takes VALUES(3, 1002, 2024, 'first', 88, 'B+');
INSERT INTO takes VALUES(4, 1003, 2022, 'summer', 92, 'A');
INSERT INTO takes VALUES(5, 1004, 2023, 'second', 78, 'C+');
INSERT INTO takes VALUES(6, 1005, 2024, 'summer', 85, 'B');
INSERT INTO takes VALUES(2, 1005, 2021, 'first', 90, 'A');
/*-------------------------------------------------------------------------------------------*/
INSERT INTO instractor VALUES(10000, 'elhosany', 35,50000,100);
INSERT INTO instractor VALUES(10001, 'ahmed', 40, 6000, 100);
INSERT INTO instractor VALUES(10002, 'samy', 45, 5000, 101);
INSERT INTO instractor VALUES(10003, 'nada', 30, 48000, 102);
/*-------------------------------------------------------------------------------------------*/
INSERT INTO gives VALUES(10000,1000);
INSERT INTO gives VALUES(10000,1001);
INSERT INTO gives VALUES(10001,1002);
INSERT INTO gives VALUES(10002,1003);
INSERT INTO gives VALUES(10003,1004);
INSERT INTO gives VALUES(10003,1005);
/*-------------------------------------------------------------------------------------------*/

SELECT * FROM students;
SELECT * FROM program;
SELECT * FROM courses;
SELECT * FROM takes;
SELECT * FROM instractor;
SELECT * FROM gives;


select * from students join program
where students.prog_id=program.program_id;


create table A select * from students join takes
where students.student_id=takes.stud_id;

select * from A;

select * from A join courses
where A.cour_id=courses.courses_id;

select student_id,CONCAT(fname, ' ', mname, ' ', lname) AS Name,semster,mark,grade,courses_name,point_courses from A join courses
where A.cour_id=courses.courses_id;

