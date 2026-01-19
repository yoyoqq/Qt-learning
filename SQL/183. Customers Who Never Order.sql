# Write your MySQL query statement below
SELECT c.name as Customers
FROM Customers c
LEFT JOIN Orders o ON o.customerId = c.id
-- WHERE o.id IS NULL
WHERE o.customerId IS NULL
;

-- c.id c.name o.id o.customerId
-- 1 Alice NULL NULL
-- 2 Bob 10 2

-- orders.customerId NOT IN Customers.id 
-- SELECT c.name 
-- FROM Customers AS c 
-- LEFT JOIN Orders as o ON c.id = o.id
-- WHERE o.id NOT IN c.id