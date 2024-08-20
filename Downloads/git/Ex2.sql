CREATE DATABASE Ex2;
GO
USE SSJAVA;

CREATE TABLE Department(
	id				INT IDENTITY(1,1) PRIMARY KEY,
	departmentName	NVARCHAR(50) NOT NULL,
)

CREATE TABLE Customer(
	id				INT IDENTITY(1,1) PRIMARY KEY,
	username		VARCHAR(25) UNIQUE NOT NULL,
	customerName	NVARCHAR(50) NOT NULL,
	email			NVARCHAR(25),
	phone			VARCHAR(10),
	password		VARCHAR(100) NOT NULL,
	departmentId	INT,
	FOREIGN KEY (departmentId) REFERENCES Department(id)
)

CREATE PROCEDURE spGetCustomerByEmail
	@Email nvarchar(250)
AS
BEGIN
	--Set NOCOUNT ON added to prevent extra result sets from
	--interfering with SELECT statement
	SET NOCOUNT ON
	
	SELECT * FROM [dbo].[Customer] WHERE email = @Email
END
GO

SELECT * FROM Customer;

UPDATE Customer
SET password = '123456789'

ALTER TABLE Customer
ADD UNIQUE (username);