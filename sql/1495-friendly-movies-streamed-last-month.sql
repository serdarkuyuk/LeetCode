# Write your MySQL query statement below
SELECT DISTINCT(Content.title)
FROM Content, TVProgram
WHERE TVProgram.program_date >= "2020-06-01 " AND TVProgram.program_date < "2020-07-01"
AND Content.Kids_content = "Y"
AND Content.content_type = "Movies"
AND Content.content_id = TVProgram.content_id



SELECT DISTINCT(Content.title)
FROM Content
JOIN TVProgram
ON Content.content_id = TVProgram.content_id
# WHERE TVProgram.program_date >= "2020-06-01 " AND TVProgram.program_date < "2020-07-01"
WHERE TVProgram.program_date LIKE "2020-06%" # AND TVProgram.program_date < "2020-07-01"
AND Content.Kids_content = "Y"
AND Content.content_type = "Movies"
