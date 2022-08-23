use employees_demo;

DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees (
	EmployeeId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Firstname VARCHAR(25),
    Lastname VARCHAR(25),
    ReportsTo INT,
	Dept VARCHAR(25),
	Salary DECIMAL(6,2),
    
    CONSTRAINT FK_ReportsTo_EmployeeID FOREIGN KEY (ReportsTo, Dept, Salary) REFERENCES Employees(EmployeeID)
);

INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('John', 'Smith', null, 'Sales', 3200);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Mary', 'Jane', 1, 'IT', 2400);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Joe', 'Kuther', 1, 'HR', 2120);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Joe', 'Kuther', 2, 'Finance', 3000);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Neo', 'Anderson', 3, 'Sales', 2650);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Trinity', 'Carrie', 3, 'IT', 3000);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Tony', 'Stark', 4, 'HR', 2500);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Bruce', 'Banner', 6, 'Finance', 2300);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Scott', 'Lang', 6, 'Sales', 2350);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Bucky', 'Barnes', 9, 'IT', 2900);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Jane', 'Foster', 8, 'HR', 2900);
INSERT INTO Employees (Firstname, Lastname, ReportsTo, Dept, Salary) VALUES ('Maria', 'Hill', 9, 'Finance', 2560);

