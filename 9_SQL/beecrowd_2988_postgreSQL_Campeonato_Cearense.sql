SELECT 
    teams.name, 
    COUNT(matches.id) AS matches,
    SUM (
        CASE
            WHEN (teams.id = matches.team_1 AND matches.team_1_goals > matches.team_2_goals)
            OR (teams.id = matches.team_2 AND matches.team_2_goals > matches.team_1_goals)
            THEN 1
            ELSE 0
        END
    ) AS victories,
    SUM (
        CASE
            WHEN (teams.id = matches.team_1 AND matches.team_1_goals < matches.team_2_goals)
            OR (teams.id = matches.team_2 AND matches.team_2_goals < matches.team_1_goals)
            THEN 1
            ELSE 0
        END
    ) AS defeats,
    SUM (
        CASE
            WHEN (matches.team_1_goals = matches.team_2_goals) THEN 1
            ELSE 0
        END
    ) AS draws,
    SUM(
        CASE 
            WHEN (teams.id = matches.team_1 AND matches.team_1_goals > matches.team_2_goals)
            OR (teams.id = matches.team_2 AND matches.team_2_goals > matches.team_1_goals)
            THEN 3
            WHEN (matches.team_1_goals = matches.team_2_goals) THEN 1
            ELSE 0
        END
    ) AS score
    FROM teams
    JOIN matches ON teams.id = matches.team_1 OR teams.id = matches.team_2
    GROUP BY teams.name
    ORDER BY score DESC, teams.name ASC;