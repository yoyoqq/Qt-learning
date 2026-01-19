/*
Clients
client_id	name
1	Alice
2	Bob
3	Carol
4	David
5	Emma
6	Frank

Investments
investment_id	client_id	amount
1	1	5000
2	1	2000
3	2	10000
4	3	3000
5	3	7000
6	4	12000
7	5	4000
8	5	6000
9	6	1500
*/

/* 

1. sum investment per client
2. rank client taht sum 
3. return top 5 
 */

SELECT c.client_id, c.name, SUM(i.amount) as investments
FROM Clients c
JOIN Investments i ON c.client_id = i.client_id
GROUP BY c.client_id 
ORDER BY SUM(i.amount) DESC
LIMIT 5
;
