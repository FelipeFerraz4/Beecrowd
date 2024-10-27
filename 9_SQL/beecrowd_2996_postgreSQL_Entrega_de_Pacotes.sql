SELECT packages.year, users1.name AS sender, users2.name AS receiver FROM packages
    JOIN users users1 ON packages.id_user_sender = users1.id
    JOIN users users2 ON packages.id_user_receiver = users2.id
    WHERE (packages.color = 'blue' OR packages.year = 2015)
    AND users1.address != 'Taiwan'
    AND users2.address != 'Taiwan'
    ORDER BY packages.year DESC;