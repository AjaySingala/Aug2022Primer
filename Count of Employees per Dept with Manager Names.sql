USE Employees;

select
	e2.emp_no,e2.first_name,e2.last_name,d.dept_name,count(de.emp_no) - 1 as NumEmp
from employees e 
	join dept_emp de on de.emp_no = e.emp_no
	join departments d on d.dept_no = de.dept_no 
	join dept_manager dm on d.dept_no = dm.dept_no
    join employees e2 on dm.emp_no = e2.emp_no
where 1=1
AND dm.to_date = '9999-01-01' 
and de.to_date = '9999-01-01'
group by d.dept_no;

