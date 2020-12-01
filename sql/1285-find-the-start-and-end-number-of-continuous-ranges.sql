# Write your MySQL query statement below
SELECT
    MIN(temp.log_id) AS start_id,
    MAX(temp.log_id) AS end_id
FROM
    (
    SELECT
        log_id,
        ROW_NUMBER() OVER (ORDER BY log_id) AS row_numberS
    FROM
        logs
    ) temp
GROUP BY
    (log_id - row_numberS)
ORDER BY
    start_id
 
