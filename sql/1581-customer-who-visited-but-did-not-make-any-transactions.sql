# Write your MySQL query statement below
SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM Visits
LEFT JOIN
    Transactions
USING (visit_id)
WHERE amount is null
GROUP BY customer_id
