with media_salariais AS (
    SELECT
        departamento.nome AS "departamento", 
        divisao.nome AS "divisao",
        ROUND(AVG(valor_bruto.Salario_Bruto - valor_desconto.Total_Desconto), 2) AS "media"
        FROM empregado
    INNER JOIN departamento ON empregado.lotacao = departamento.cod_dep
    INNER JOIN divisao ON empregado.lotacao_div = divisao.cod_divisao 
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
    GROUP BY departamento.nome, divisao.nome
),
maior_por_departamento AS (
    SELECT
        media_salariais.departamento,
        media_salariais.divisao,
        media_salariais.media,
        ROW_NUMBER() OVER (PARTITION BY media_salariais.departamento ORDER BY media_salariais.media DESC) AS numero_return
    FROM media_salariais
)

SELECT 
    maior_por_departamento.departamento, 
    maior_por_departamento.divisao, 
    maior_por_departamento.media
    FROM maior_por_departamento
    WHERE numero_return = 1
    ORDER BY maior_por_departamento.media DESC;