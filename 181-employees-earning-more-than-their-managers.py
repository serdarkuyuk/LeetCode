# Write your MySQL query statement below
SELECT e2.Name AS Employee
FROM Employee e1
JOIN Employee e2
ON e1.Id = e2.ManagerId
WHERE e1.Salary < e2.salary
