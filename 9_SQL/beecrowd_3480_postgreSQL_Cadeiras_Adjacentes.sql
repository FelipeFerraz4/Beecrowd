SELECT chairs.queue, chairs.id as "left", chairs2.id as "right" 
    FROM chairs 
    JOIN chairs chairs2 ON chairs.queue = chairs2.queue AND chairs.id = chairs2.id - 1 
    WHERE chairs.available = TRUE AND chairs2.available = TRUE 
    ORDER BY "left";