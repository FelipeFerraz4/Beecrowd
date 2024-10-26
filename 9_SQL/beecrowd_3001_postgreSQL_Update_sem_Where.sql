WITH products_a AS (
    SELECT 
        products.name,
        ROUND(20, 1) AS price
    FROM products
    WHERE products.type = 'A'
    ORDER BY products.id DESC 
),
products_b AS (
    SELECT 
        products.name,
        ROUND(70, 1) AS price
    FROM products
    WHERE products.type = 'B'
    ORDER BY products.id DESC 
),
products_c AS (
    SELECT 
        products.name,
        ROUND(530.5, 1) AS price
    FROM products
    WHERE products.type = 'C'
    ORDER BY products.id DESC 
)

SELECT * FROM products_a
UNION ALL
SELECT * FROM products_b
UNION ALL
SELECT * FROM products_c;