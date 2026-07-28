{{ config(materialized='ephemeral') }}

SELECT
    user_id
FROM {{ source('bronze','ab_test') }}
WHERE
    (con_treat = 'control' AND page = 'old_page')
    OR
    (con_treat = 'treatment' AND page = 'new_page')
GROUP BY user_id
HAVING COUNT(DISTINCT con_treat) = 1 AND COUNT(DISTINCT page) = 1