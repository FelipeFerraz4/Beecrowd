SELECT records.temperature, Count(*) AS number_of_records FROM records
    GROUP BY records.temperature, records.mark
    ORDER BY MIN(records.id);