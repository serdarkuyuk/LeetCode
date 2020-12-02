# Write your MySQL query statement below
SELECT project_id, employee_id
FROM (
    SELECT
        p.project_id,
        p.employee_id,
        e.experience_years,
        RANK() OVER(PARTITION BY project_id ORDER BY experience_years DESC) AS rnk
FROM
    Project p
LEFT JOIN
    Employee e
Using (employee_id)
     ) t
WHERE rnk = 1
