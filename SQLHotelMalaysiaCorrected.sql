CREATE DATABASE Hotel_Malaysia; 

go 
USE Hotel_Malaysia

CREATE TABLE Guests( 

Guest_ID int IDENTITY(1,1) PRIMARY KEY, 

Guest_LName varchar(255) NOT NULL, 

Guest_FName varchar(255), 

Guest_DOB date, 

Guest_Address_1 varchar(255), 

Guest_Address_2 varchar(255), 

Guest_City nvarchar(255), 

Guest_Country nvarchar(255), 

Guest_Postal_Code varchar(255), 

Guest_Passport_No varchar(255), 

Guest_Email_fax varchar(255), 

Guest_Phone int, 

Guest_Nationality varchar (255) 

); 

go 

 INSERT INTO Guests (Guest_LName,Guest_FName,Guest_DOB,Guest_Passport_No,Guest_Phone,Guest_Email_fax,Guest_Postal_Code,Guest_Address_1,Guest_City,Guest_Country,Guest_Nationality)
 VALUES ('Bui Ha','Tan','1987-03-22','1234567','1902123456','T@gmail.com','1B34E6','123 Bedford Highway','Halifax','Canada','Vietnamese'), ('Gannamani','Raghu Ram','1995-12-17','7654321','1902765432','R@gmail.com','6E43B1','456 Lady Hammond Dr','Halifax','Canada','Indian');

CREATE TABLE Bookings( 

Booking_ID int IDENTITY(1,1) PRIMARY KEY, 

Booking_Type varchar(255), 

Guest_ID_FK int FOREIGN KEY REFERENCES Guests(Guest_ID) 

); 

go 

 INSERT INTO Bookings(Booking_Type,Guest_ID_FK)
 VALUES ('New Booking',1),('Amendmant',2);

CREATE TABLE Room( 

Room_ID int IDENTITY(1,1) PRIMARY KEY, 

Room_Name varchar(255), 

Room_Type varchar(255), 

Room_Rate int, 

Special_Reqs varchar(255), 

Room_Arrival_Date date, 

Room_Departure_Date date, 

Booking_ID_FK int FOREIGN KEY REFERENCES Bookings(Booking_ID) 

); 
go 

 INSERT INTO Room(Room_Name,Room_Type,Special_Reqs,Room_Arrival_Date,Room_Departure_Date,Booking_ID_FK)
 VALUES ('Rose Room','penthouse','non-smoking','2021-04-15','2021-05-01',1);

CREATE TABLE Travel( 

Travel_ID int IDENTITY(1,1) PRIMARY KEY, 

Booking_ID_FK int FOREIGN KEY REFERENCES Bookings(Booking_ID), 

Airport_Pickup bit,

Airport_Dropoff bit,

Flight_Arrival datetime, 

Flight_Departure datetime 

); 
go 

INSERT INTO Travel(Booking_ID_FK,Airport_Pickup,Airport_Dropoff,Flight_Arrival,Flight_Departure)
VALUES (1,1,1,'2021-04-15 08:00:00','2021-05-01 08:00:00')

 
CREATE TABLE Pay( 

Pay_ID int IDENTITY(1,1) PRIMARY KEY, 

Name_on_Card nvarchar(255), 

Card_Num int, 

Card_Type varchar(255), 

Card_EXP_date date, 

Card_Sec_code int, 

Card_Sig nvarchar(255), 

Guest_ID_FK int FOREIGN KEY REFERENCES Guests(Guest_ID) 
);
