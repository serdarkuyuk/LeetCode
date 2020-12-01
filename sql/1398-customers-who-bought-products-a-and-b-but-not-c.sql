# Write your MySQL query statement below

SELECT
    o.customer_id,
    c.customer_name
FROM
    Orders o
LEFT JOIN
    Customers c
USING
    (customer_id)
GROUP BY
    customer_id
HAVING
    SUM(o.product_name = "A")>0 AND SUM(o.product_name = "B")>0 and SUM(o.product_name = "C")=0

SELECT customer_id, customer_name
FROM Customers
WHERE (customer_id in (SELECT customer_id FROM Orders WHERE product_name = "A"))
AND (customer_id in (SELECT customer_id FROM Orders WHERE product_name = "B"))
AND (customer_id NOT in (SELECT customer_id FROM Orders WHERE product_name = "C"))
