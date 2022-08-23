use employees;

SELECT d.dept_no, AVG(s.salary)
FROM departments d
JOIN dept_emp de ON d.dept_no = de.dept_no
JOIN salaries s ON de.emp_no = s.emp_no
WHERE s.to_date = '9999-01-01'
AND de.to_date = '9999-01-01'
GROUP BY d.dept_no
ORDER BY d.dept_no;

SELECT e.emp_no, e.first_name, e.last_name, s.salary, d.dept_no, d.dept_name
FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments d ON de.dept_no = d.dept_no
JOIN Salaries s ON e.emp_no = s.emp_no,
	( 
		SELECT d.dept_no, AVG(s.salary) as 'AvgSalary'
		FROM departments d
		JOIN dept_emp de ON d.dept_no = de.dept_no
		JOIN salaries s ON de.emp_no = s.emp_no
		WHERE s.to_date = '9999-01-01'
		AND de.to_date = '9999-01-01'
		GROUP BY d.dept_no
	) e2
WHERE e2.dept_no = d.dept_no
AND s.salary > e2.AvgSalary
AND s.to_date = '9999-01-01'
AND de.to_date = '9999-01-01'
-- ORDER BY d.dept_no