-- Write a query in SQL to find the number of matches ending with only one goal win except those matches which was decided by penalty shootout.(match_details)
SELECT COUNT(match_no)
FROM match_details
WHERE win_lose = 'W' AND goal_score = 1;

EXCEPT

SELECT match_no
FROM match_details
WHERE decided_by = 'P';