# Write your MySQL query statement below
SELECT w2.id
FROM Weather w1, Weather w2
WHERE DATE_ADD(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate AND w2.Temperature > w1.Temperature

# SELECT w2.id  #, DATEDIFF(w1.recordDate, w2.recordDate)
# FROM Weather w1
# JOIN Weather w2
# ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
# AND w2.Temperature > w1.Temperature

SELECT t1.Id
FROM Weather t1
INNER JOIN Weather t2
ON TO_DAYS(t1.recordDate) = TO_DAYS(t2.recordDate) + 1
WHERE t1.Temperature > t2.Temperature
