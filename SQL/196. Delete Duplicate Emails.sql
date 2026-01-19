# Write your MySQL query statement below
DELETE p 
FROM Person p
JOIN Person r
ON  p.email = r.email
AND p.id > r.id
;

-- SELECT p.id, p.email
-- FROM PERSON p
-- JOIN Person r
-- DELETE FROM p
-- WHERE p.id < r.id
-- ;