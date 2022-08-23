use employees_demo;

WITH cte_Top5Employees
AS (
	SELECT e.Firstname, e.Lastname, e.Salary,
		-- RANK() OVER (ORDER BY e.Salary) AS RowNumber
		DENSE_RANK() OVER (ORDER BY e.Salary) AS RowNumber
	FROM Employees e
)
SELECT * FROM cte_Top5Employees c
WHERE c.RowNumber <= 5


