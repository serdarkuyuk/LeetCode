# Write your MySQL query statement below

SELECT student_id, course_id, grade
FROM (SELECT *,
    row_number() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id) as row_num
FROM Enrollments) as s
WHERE row_num = 1
