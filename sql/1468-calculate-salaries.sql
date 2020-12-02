# Write your MySQL query statement below
SELECT s.company_id, s.employee_id, s.employee_name,
round(
    CASE
    WHEN x.xsalary > 10000 THEN 0.51*salary
    WHEN x.xsalary >= 1000 AND salary <= 10000 THEN 0.76*salary
    ELSE salary
    END
) as salary
FROM Salaries s
INNER JOIN (
            SELECT company_id, MAX(salary) as xsalary
            FROM Salaries
            GROUP BY company_id
            ) as x
USING (company_id)
