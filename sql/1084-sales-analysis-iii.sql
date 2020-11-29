# Write your MySQL query statement below
# SELECT P.product_id, P.product_name, S.sale_date
# From Product P
# JOIN Sales S
# ON P.product_id = S.product_id
# GROUP BY S.product_id, P.product_name
# HAVING MAX(sale_date) >= "2019-01-01" AND MIN(sale_date) <="2019-03-31";

SELECT product_id, product_name
FROM Product
WHERE product_id NOT IN
(
    SELECT product_id
    FROM Sales
    WHERE  sale_date > '2019-03-31' OR sale_date < '2019-01-01'
);

# select s.product_id, p.product_name  #, S.sale_date
# from sales s, product p
# where s.product_id = p.product_id
# group by s.product_id  #, p.product_name
# having min(s.sale_date) >= '2019-01-01'
#     and max(s.sale_date) <= '2019-03-31'
