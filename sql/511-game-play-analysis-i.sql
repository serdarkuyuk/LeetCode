# Write your MySQL query statement below
SELECT T.player_id, T.event_date AS first_login
FROM (
    SELECT player_id, event_date,
    RANK() OVER(PARTITION BY player_id ORDER BY event_date) as rnk
    FROM activity
    ) AS T
WHERE rnk = 1

SELECT player_id, MIN(event_date) AS first_login
FROM activity
GROUP BY player_id
