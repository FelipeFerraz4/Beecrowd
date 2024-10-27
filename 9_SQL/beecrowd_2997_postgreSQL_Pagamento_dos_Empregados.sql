SELECT 
    departamento.nome AS "Departamento", 
    empregado.nome AS "Empregado",
    valor_bruto.Salario_Bruto AS "Salario Bruto",
    valor_desconto.Total_Desconto AS "Total Desconto",
    (valor_bruto.Salario_Bruto - valor_desconto.Total_Desconto) AS "Salario Liquido"
    FROM
        empregado
    INNER JOIN 
        departamento ON empregado.lotacao = departamento.cod_dep
    INNER JOIN (
        SELECT empregado.matr, COALESCE(SUM(vencimento.valor), 0) AS Salario_Bruto
        FROM empregado
        LEFT JOIN emp_venc ON emp_venc.matr = empregado.matr
        LEFT JOIN vencimento ON vencimento.cod_venc = emp_venc.cod_venc
        GROUP BY empregado.matr
    ) AS valor_bruto ON empregado.matr = valor_bruto.matr
    INNER JOIN (
        SELECT empregado.matr, COALESCE(SUM(desconto.valor), 0) AS Total_Desconto
        FROM empregado
        LEFT JOIN emp_desc ON emp_desc.matr = empregado.matr
        LEFT JOIN desconto ON emp_desc.cod_desc = desconto.cod_desc
        GROUP BY empregado.matr
    ) AS valor_desconto ON empregado.matr = valor_desconto.matr
    GROUP BY 
        empregado.matr, departamento.nome, empregado.nome, valor_bruto.Salario_Bruto, valor_desconto.Total_Desconto
    ORDER BY 
        (valor_bruto.Salario_Bruto - valor_desconto.Total_Desconto) DESC;
