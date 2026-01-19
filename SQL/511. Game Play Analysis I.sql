# Write your MySQL query statement below
-- SELECT a1.player_id, event_date as first_login 
-- FROM Activity a1, Activity a2
-- WHERE a1.recordDate < a2.recordDate 
-- ;

SELECT a1.player_id, MIN(event_date) as first_login
FROM Activity a1
GROUP BY a1.player_id
;