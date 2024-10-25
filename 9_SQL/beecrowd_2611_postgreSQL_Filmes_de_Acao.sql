SELECT movies.ID , movies.NAME FROM movies 
    JOIN genres ON genres.ID = movies.id_genres
    WHERE genres.description = 'Action';