# Write your MySQL query statement below
WITH RECURSIVE CTE AS(

    SELECT employee_id, 1 AS lvl
    FROM Employees
    WHERE manager_id = 1 AND employee_id <> 1

    UNION ALL

    SELECT e.employee_id, c.lvl + 1 AS lvl
    FROM CTE c
    JOIN Employees e
    ON c.employee_id = e.manager_id

)
SELECT employee_id
FROM CTE
WHERE lvl <= 3
ORDER BY employee_id
