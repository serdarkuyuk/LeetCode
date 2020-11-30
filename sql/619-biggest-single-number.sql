#Write your MySQL query statement below
SELECT
(
    SELECT num
    FROM my_numbers
    GROUP BY num
    HAVING COUNT(num) < 2
    ORDER BY num DESC
    LIMIT 1
) AS NUM



SELECT IFNULL(
                (
                    SELECT num
                    FROM my_numbers
                    GROUP BY num
                    HAVING COUNT(num) < 2
                    ORDER BY num DESC
                    LIMIT 1
                ),
            null
            ) AS num


SELECT MAX(NUM) AS num
FROM
(
SELECT num
FROM my_numbers
GROUP BY num
HAVING COUNT(num) < 2
) AS num
