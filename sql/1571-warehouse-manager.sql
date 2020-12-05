# Write your MySQL query statement below
SELECT w.name AS WAREHOUSE_NAME, SUM(w.units*(p.Width*p.Length*p.Height)) as VOLUME
FROM Warehouse w
JOIN Products p
USING (product_id)
GROUP BY w.name
