use employees_demo;

SELECT Dept, AVG(Salary)
FROM Employees e2
GROUP BY Dept;

SELECT EmployeeId, Firstname, Lastname, Dept, Salary
FROM Employees e1;

SELECT EmployeeId, Firstname, Lastname, Dept, Salary
FROM Employees e1
WHERE Salary > (
	SELECT AVG(Salary)
    FROM Employees e2
    WHERE e2.Dept = e1.Dept
);


