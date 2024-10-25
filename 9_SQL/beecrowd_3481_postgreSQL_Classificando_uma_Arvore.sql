WITH nodetypes AS (
    SELECT DISTINCT node_id,
    CASE
        WHEN node_id NOT in (SELECT node_id FROM ( SELECT node_id FROM nodes WHERE pointer IS NULL UNION ALL SELECT pointer AS node_id FROM nodes WHERE pointer IS NOT NULL ) AS combined_results GROUP BY node_id)  THEN 'ROOT'
        WHEN pointer IS NOT NULL THEN 'INNER'
        WHEN pointer IS NULL THEN 'LEAF'
    END AS type
    FROM nodes
)

SELECT node_id, type FROM nodetypes ORDER BY node_id;