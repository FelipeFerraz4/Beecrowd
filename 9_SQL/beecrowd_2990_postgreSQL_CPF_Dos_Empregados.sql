  SELECT empregados.cpf, empregados.enome, departamentos.dnome FROM empregados
    JOIN departamentos ON departamentos.dnumero = empregados.dnumero
    WHERE empregados.cpf NOT IN (SELECT trabalha.cpf_emp AS cpf FROM trabalha) 
    ORDER BY empregados.cpf ASC;