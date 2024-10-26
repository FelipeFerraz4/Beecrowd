SELECT 
    SUBSTRING(natural_person.cpf FROM 1 FOR 3) || '.' ||
    SUBSTRING(natural_person.cpf FROM 4 FOR 3) || '.' ||
    SUBSTRING(natural_person.cpf FROM 7 FOR 3) || '-' ||
    SUBSTRING(natural_person.cpf FROM 10 FOR 2) AS CPF
    FROM natural_person;