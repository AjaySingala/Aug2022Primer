USE Employees;

WITH cte_rank_salary
AS (
	SELECT 
		e.emp_no, e.First_name, e.Last_name
		, t.title
		, s.salary
		, de.dept_no
		, d.dept_name
		, DENSE_RANK() OVER (ORDER BY s.salary DESC) SalaryRank
	FROM Employees e
	INNER JOIN titles t ON e.emp_no = t.emp_no
	INNER JOIN salaries s ON e.emp_no = s.emp_no
	INNER JOIN dept_emp de ON e.emp_no = de.emp_no
	INNER JOIN departments d ON de.dept_no = d.dept_no
	WHERE 1=1 
	AND de.to_date = '9999-01-01'
	AND t.to_date = '9999-01-01'
	AND s.to_date = '9999-01-01'
)
SELECT * FROM cte_rank_salary
WHERE SalaryRank <= 5
