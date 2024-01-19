-- 3.2. Write a query in SQL to find the winner of EURO cup 2016. (soccer_country, match_details)
SELECT
    c.country_name AS winner_2016_eurocup
FROM
    soccer_country c
WHERE
    c.country_id = (
        SELECT
            md.team_id
        FROM
            match_details md
        WHERE
            md.play_stage = 'F' -- Assuming 'F' represents the final stage
            AND md.win_lose = 'W'
            AND md.goal_score = (
                SELECT
                    MAX(goal_score)
                FROM
                    match_details
                WHERE
                    play_stage = 'F' -- Assuming 'F' represents the final stage
            )
    );