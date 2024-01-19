-- 2. Write a query in SQL to find the number of goal scored by each team in every match within normal play schedule.  (match_details, soccer_country)
SELECT
    md.match_no,
    md.team_id,
    sc.country_name AS team_name,
    md.goal_score AS goals_scored
FROM
    match_details md
JOIN
    soccer_country sc ON md.team_id = sc.country_id
WHERE
    md.decided_by = 'N';