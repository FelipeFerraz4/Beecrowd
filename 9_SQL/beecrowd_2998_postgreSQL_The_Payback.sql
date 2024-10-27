WITH total_profit AS (
    SELECT
        clients.id,
        clients.name,
        clients.investment,
        operations.month,
        SUM(operations.profit) OVER (PARTITION BY operations.client_id ORDER BY operations.month) AS cumulative_profit
        FROM clients
        JOIN operations ON operations.client_id = clients.id
),
payback_month AS (
    SELECT
        total_profit.name,
        total_profit.investment,
        total_profit.month AS month_of_payback,
        total_profit.cumulative_profit - total_profit.investment AS return_value,
        ROW_NUMBER() OVER (PARTITION BY total_profit.id ORDER BY total_profit.month) AS number_return
    FROM total_profit
    WHERE total_profit.cumulative_profit >= total_profit.investment
)

SELECT
    payback_month.name,
    payback_month.investment,
    payback_month.month_of_payback,
    payback_month.return_value AS "return"
    FROM payback_month
    WHERE number_return = 1
    ORDER BY return_value DESC;
