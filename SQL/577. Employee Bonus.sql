# Write your MySQL query statement below
# no bonus, or less than 1000
SELECT e.name, b.bonus
FROM Employee e 
LEFT JOIN Bonus b on e.empId = b.empId
WHERE b.bonus < 1000
OR b.empId IS NULL
;