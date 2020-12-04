# Write your MySQL query statement below
SELECT  DATE_FORMAT(order_date,'%Y-%m') as month,
        COUNT(invoice) AS order_count,
        COUNT(DISTINCT customer_id) AS customer_count
FROM
    Orders
WHERE
    invoice > 20
GROUP BY 1 #YEAR(order_date), MONTH(order_date)
