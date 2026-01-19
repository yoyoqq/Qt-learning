# Write your MySQL query statement below
SELECT e.name 
FROM Employee AS e                          # m.id is the id of the e.ids linked..
JOIN Employee AS m ON e.managerId = m.id    # self join table, get mangaers 
WHERE e.salary > m.salary                   # compare to its respective managers 
;



-- SELECT name 
-- FROM Employee as e 
-- WHERE e.salary >= X, e.managerId IS NULL 
-- HAVING e.salary >= MAX(salary), e.managerId IS NOT NULL 

-- ;
-- AND is logical, not selector
-- IS NULL / IS NOT NULL 
-- WHERE (salary AND managerId = NULL) >= MAX(salary AND managerId != NULL) 