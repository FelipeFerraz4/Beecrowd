with city AS (
    SELECT 
        cities.city_name, 
        cities.population,
        ROW_NUMBER() OVER (ORDER BY cities.population ASC) AS city_asc,
        ROW_NUMBER() OVER (ORDER BY cities.population DESC) AS city_desc
    FROM cities
)

SELECT city.city_name, city.population FROM city
    WHERE city_asc = 2 OR city_desc = 2
    ORDER BY city.population DESC;