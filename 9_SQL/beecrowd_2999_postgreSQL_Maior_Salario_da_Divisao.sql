with salario_bruto AS (
    SELECT empregado.matr, COALESCE(SUM(vencimento.valor), 0) AS Salario_Bruto
        FROM empregado
        LEFT JOIN emp_venc ON emp_venc.matr = empregado.matr
        LEFT JOIN vencimento ON vencimento.cod_venc = emp_venc.cod_venc
        GROUP BY empregado.matr
),
desconto_salario AS (
    SELECT empregado.matr, COALESCE(SUM(desconto.valor), 0) AS Total_Desconto
        FROM empregado
        LEFT JOIN emp_desc ON emp_desc.matr = empregado.matr
        LEFT JOIN desconto ON emp_desc.cod_desc = desconto.cod_desc
        GROUP BY empregado.matr
),
media_salariais AS (
    SELECT
        departamento.nome AS departamento, 
        divisao.nome AS divisao,
        ROUND(AVG(valor_bruto.Salario_Bruto - valor_desconto.Total_Desconto), 2) AS media
        FROM empregado
    INNER JOIN departamento ON empregado.lotacao = departamento.cod_dep
    INNER JOIN divisao ON empregado.lotacao_div = divisao.cod_divisao 
    INNER JOIN salario_bruto AS valor_bruto ON empregado.matr = valor_bruto.matr
    INNER JOIN desconto_salario AS valor_desconto ON empregado.matr = valor_desconto.matr
    GROUP BY departamento.nome, divisao.nome
),
empregados_salarios AS (
    SELECT 
        departamento.nome AS departamento,
        divisao.nome AS divisao,
        empregado.nome AS nome,
        empregado.lotacao_div,
        (valor_bruto.Salario_Bruto - valor_desconto.Total_Desconto) AS Salario_Liquido
        FROM empregado
        INNER JOIN departamento ON empregado.lotacao = departamento.cod_dep
        INNER JOIN divisao ON empregado.lotacao_div = divisao.cod_divisao 
        INNER JOIN salario_bruto AS valor_bruto ON empregado.matr = valor_bruto.matr
        INNER JOIN desconto_salario AS valor_desconto ON empregado.matr = valor_desconto.matr
)

SELECT empregados_salarios.nome, empregados_salarios.Salario_Liquido
    FROM empregados_salarios
    JOIN media_salariais ON media_salariais.departamento = empregados_salarios.departamento 
    AND media_salariais.divisao = empregados_salarios.divisao 
    WHERE empregados_salarios.Salario_Liquido > media_salariais.media AND empregados_salarios.Salario_Liquido >= 8000
    ORDER BY empregados_salarios.lotacao_div;