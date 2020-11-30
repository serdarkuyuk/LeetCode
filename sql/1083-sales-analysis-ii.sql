SELECT cnt as buyer_id
FROM
(
    SELECT s.buyer_id AS cnt, p.product_name
    FROM Sales s
    INNER JOIN Product p
    ON s.product_id = p.product_id
    GROUP BY s.buyer_id
    HAVING COUNT(DISTINCT(s.product_id)) = 1
)
AS M
WHERE M.product_name = "S8"



# Write your MySQL query statement below
SELECT DISTINCT buyer_id
FROM Sales
JOIN Product
USING (product_id)
WHERE product_name = "S8"
AND buyer_id NOT IN
(
    SELECT DISTINCT buyer_id
    FROM Sales
    JOIN Product
    USING (product_id)
    WHERE product_name = "IPhone"
    )iPhone' )
