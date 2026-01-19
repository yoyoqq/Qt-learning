# Write your MySQL query statement below
# refered != 2 or any customer 
SELECT c.name 
FROM Customer c 
WHERE c.referee_id != 2 OR c.referee_id IS NULL
;