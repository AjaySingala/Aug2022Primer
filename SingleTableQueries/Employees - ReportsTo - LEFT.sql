use employees_demo;

SELECT 
	e1.EmployeeId, e1.Firstname, e1.Lastname, e1.ReportsTo,
    e2.EmployeeId, e2.Firstname, e2.Lastname
FROM Employees e1
LEFT JOIN Employees e2 ON e1.ReportsTo = e2.EmployeeId
