# Write your MySQL query statement below
SELECT name,
    SUM(rest) as rest,
    SUM(paid) as paid,
    SUM(canceled) as canceled,
    SUM(refunded) as refunded
FROM Product
JOIN Invoice
USING (product_id)
GROUP BY product_id
ORDER BY name
