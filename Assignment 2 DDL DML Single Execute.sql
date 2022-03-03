CREATE DATABASE STUDENT_PROGRAM_NEW;
go
use STUDENT_PROGRAM_NEW
go
CREATE TABLE Program (
prog_ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
prog_NAME nvarchar(50)
);
CREATE TABLE Teacher(
teach_ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
teach_FNAME nvarchar(50),
teach_LNAME nvarchar(50),
teach_Addr1 nvarchar(255),
teach_Addr2 nvarchar(255),
teach_City nvarchar(50),
teach_PCODE nvarchar(50)
);
CREATE TABLE Student (
stu_ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
stu_FNAME nvarchar(50),
stu_LNAME nvarchar(50),
stu_Addr1 nvarchar(255),
stu_Addr2 nvarchar(255),
stu_City nvarchar(255),
stu_PCODE nvarchar(255),
stu_DOB nvarchar(255),
stu_FeePaid BIT,
prog_ID_FK int FOREIGN KEY REFERENCES Program (prog_ID)
);
CREATE TABLE Class (
class_ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
class_Name nvarchar(50),
teach_ID_FK int FOREIGN KEY REFERENCES Teacher (teach_ID)
);
CREATE TABLE Enrollement (
enroll_ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
stu_ID_FK int FOREIGN KEY REFERENCES Student (stu_ID),
class_ID int FOREIGN KEY REFERENCES Class (class_ID)
);
INSERT INTO Program
(prog_NAME)
VALUES('Economics'),('Computer Science'),('Medicine'),('Dentistry');

INSERT INTO Student
(stu_FNAME,stu_LNAME,stu_Addr1,stu_City,stu_PCODE,stu_DOB,stu_FeePaid,prog_ID_FK)
VALUES('John','Smith','3 Main Str','North Boston','56125','1991-08-04',1,(SELECT prog_ID FROM Program WHERE prog_NAME ='Economics') );
INSERT INTO Student
(stu_FNAME,stu_LNAME,stu_Addr1,stu_City,stu_PCODE,stu_DOB,stu_FeePaid,prog_ID_FK)
VALUES('Maria','Giffin','16 Leeds Str','South Boston','56128','1991-09-10',1,(SELECT prog_ID FROM Program WHERE prog_NAME ='Computer Science'));
INSERT INTO Student
(stu_FNAME,stu_LNAME,stu_Addr1,stu_City,stu_PCODE,stu_DOB,stu_FeePaid,prog_ID_FK)
VALUES('Susa','Johnson','12 Arrow Str','South Boston','56128','1991-01-13',0,(SELECT prog_ID FROM Program WHERE prog_NAME ='Medicine'));
INSERT INTO Student
(stu_FNAME,stu_LNAME,stu_Addr1,stu_Addr2,stu_City,stu_PCODE,stu_DOB,stu_FeePaid,prog_ID_FK)
VALUES('Matt','Long','14 Milk Lane','A','South Boston','56128','1991-04-25',1,(SELECT prog_ID FROM Program WHERE prog_NAME ='Dentistry'));
INSERT INTO Student
(stu_FNAME,stu_LNAME,prog_ID_FK)
VALUES('Bobby',' Marley',(SELECT prog_ID FROM Program WHERE prog_NAME ='Dentistry'));
INSERT INTO Student
(stu_FNAME,stu_LNAME)
VALUES('John','Smith');

INSERT INTO Teacher
(teach_FNAME,teach_LNAME , teach_Addr1,teach_Addr2, teach_City, teach_PCODE )
VALUES('James','Peterson','44 March Way','','Glebe','56100'),('Sarah','Francis','','','',''),('Shane','Cobson','105 Mist Rd','','Faulkner','56410');

INSERT INTO Class
(class_Name,teach_ID_FK)
VALUES('Economics1',(SELECT teach_ID FROM Teacher WHERE teach_FNAME='James')),
('Biology1',(SELECT teach_ID FROM Teacher WHERE teach_FNAME='James')),('Business Intro',(SELECT teach_ID FROM Teacher WHERE teach_FNAME='James')),
('Programming2',(SELECT teach_ID FROM Teacher WHERE teach_FNAME='James')),('Biology2',(SELECT teach_ID FROM Teacher WHERE teach_FNAME='Sarah'));

INSERT INTO Enrollement
(stu_ID_FK,class_ID)
VALUES
((Select stu_ID FROM Student WHERE stu_ID = '1'),(SELECT class_ID from Class WHERE class_Name='Biology1')),
((Select stu_ID FROM Student WHERE stu_ID = '1'),(SELECT class_ID from Class WHERE class_Name='Economics1')),
((Select stu_ID FROM Student WHERE stu_ID = '2'),(SELECT class_ID from Class WHERE class_Name='Biology1')),
((Select stu_ID FROM Student WHERE stu_ID = '2'),(SELECT class_ID from Class WHERE class_Name='Business Intro')),
((Select stu_ID FROM Student WHERE stu_ID = '2'),(SELECT class_ID from Class WHERE class_Name='Programming 2')),
((Select stu_ID FROM Student WHERE stu_ID = '3'),(SELECT class_ID from Class WHERE class_Name='Biology2'));