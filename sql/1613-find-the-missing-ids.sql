# Write your MySQL query statement below
WITH RECURSIVE COUNTER AS (
    SELECT 1 AS counts

    UNION ALL

    SELECT counts+1
    FROM COUNTER
    WHERE counts < (SELECT MAX(customer_id) FROM Customers)
)

SELECT counts AS ids
FROM COUNTER
WHERE counts NOT IN (SELECT customer_id FROM Customers)
