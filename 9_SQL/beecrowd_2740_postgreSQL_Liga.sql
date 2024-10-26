WITH podium AS (
    SELECT 'Podium: ' || league.team AS name
    FROM league
    WHERE league.position <= 3
),
demoted AS (
    SELECT 'Demoted: ' || league.team AS name
    FROM league
    WHERE league.position >= (SELECT COUNT(*) FROM league) - 1
)

SELECT * FROM podium
UNION ALL
SELECT * FROM demoted;
