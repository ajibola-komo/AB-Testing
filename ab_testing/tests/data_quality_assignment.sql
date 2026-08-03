SELECT *
FROM {{ ref('silver_data_quality') }}
WHERE ABS((invalid_assignment_rate + valid_assignment_rate) - 1) > 0.0001