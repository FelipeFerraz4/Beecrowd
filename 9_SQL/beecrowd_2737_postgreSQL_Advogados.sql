WITH big AS (
    SELECT lawyers.name, lawyers.customers_number 
    FROM lawyers
    ORDER BY lawyers.customers_number DESC
    LIMIT 1
),
small AS (
    SELECT lawyers.name, lawyers.customers_number 
    FROM lawyers
    ORDER BY lawyers.customers_number ASC
    LIMIT 1
),
average AS (
    SELECT 'Average' AS name, ROUND(AVG(lawyers.customers_number)) AS customers_number 
    FROM lawyers
)

SELECT * FROM big
UNION ALL
SELECT * FROM small
UNION ALL
SELECT * FROM average;
