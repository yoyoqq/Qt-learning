# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state         # output cols 
FROM Person as p                                        # take from table 
LEFT JOIN Address as a ON p.personId = a.personId       # keep left side table  
;