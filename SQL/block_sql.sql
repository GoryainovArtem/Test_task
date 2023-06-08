---- 1)	Вывести список сотрудников, получающих заработную плату большую чем у непосредственного руководителя ----
SELECT e_1.name FROM employee e_1
JOIN employee e_2 ON e_1.chief_id = e_2.id AND e_1.salary > e_2.salary;


---- 2)	Вывести список сотрудников, получающих максимальную заработную плату в своём отделе ----
WITH salary_cte AS (
	SELECT name,
	DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as dr
	FROM employee
)
SELECT name FROM salary_cte
WHERE dr = 1;


---- 3)	Вывести список ID отделов, количество сотрудников в которых не превышает 3 человек ----
SELECT d.id FROM employee e
RIGHT JOIN department d ON d.id = e.department_id
GROUP BY d.id 
HAVING COUNT(e.id) <= 3;


---- 4)	Вывести список сотрудников, не имеющих назначенного руководителя, работающего в том-же отделе ----
SELECT e_1.name FROM employee e_1
LEFT JOIN employee e_2 ON e_1.chief_id = e_2.id
WHERE (e_2.department_id != e_1.department_id) OR (e_2.department_id IS NULL);


---- 5)	Найти список ID отделов с максимальной суммарной зарплатой сотрудников ----
SELECT department_id FROM employee 
GROUP BY department_id
HAVING SUM(salary) = (
	SELECT MAX(ts) FROM (
		SELECT SUM(salary) as ts FROM employee GROUP BY department_id
	) t
);
