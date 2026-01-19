# Write your MySQL query statement below
-- SELECT MAX(t.customer_number) AS customer_number
-- FROM (
--     SELECT o.customer_number, COUNT(*) AS times_used
--     FROM Orders o
--     GROUP BY o.customer_number
-- ) t
-- ;

-- ! GET THE AMOUNT OF TIMES A X WAS USED 
-- SELECT o.customer_number, COUNT(*) AS times_used
-- FROM Orders o 
-- GROUP BY o.customer_number
-- ;

SELECT customer_number
FROM Orders 
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1 
-- LIMIT 1 OFFSET 4        skip the top 4 return 1  
;