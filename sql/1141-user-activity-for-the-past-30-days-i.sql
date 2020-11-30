# Write your MySQL query statement below
SELECT activity_date AS "day", COUNT(DISTINCT(user_id)) AS "active_users"
FROM Activity
GROUP BY activity_date
HAVING activity_date <= '2019-07-27' AND activity_date > '2019-06-27'

select activity_date as day, count(distinct user_id) as active_users
from Activity
where datediff('2019-07-27', activity_date) <30
group by activity_date

SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY activity_date
HAVING activity_date <= '2019-07-27' AND activity_date > '2019-06-27'

SELECT activity_date AS "day", COUNT(DISTINCT(user_id)) AS "active_users"
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date
