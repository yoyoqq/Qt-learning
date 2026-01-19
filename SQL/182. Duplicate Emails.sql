# Write your MySQL query statement below
SELECT p.email
FROM Person as p
GROUP BY p.email
HAVING COUNT(*) > 1
;


-- 1. group rows by that col 
-- 2. count times it appearas
-- 3. keep only greater than 1 