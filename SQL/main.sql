SELECT customer.name 
FROM customers 
LEFT JOIN orders ON c.id = o.customer_id 
WHERE orders.id is NULL 