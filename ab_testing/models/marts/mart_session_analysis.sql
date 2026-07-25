select 
CASE
    WHEN duration_seconds < 10 THEN 'Less than 10 Sec'
    WHEN duration_seconds >= 10 AND duration_seconds < 20 THEN '10 - 19.99 Sec'
    WHEN duration_seconds >= 20 AND duration_seconds < 30 THEN '20 - 29.99 Sec'
    ELSE '30+ Sec'
END as duration_bucket,
count(distinct user_id) as total_visitors,
count(*) as total_sessions,
count(case when is_converted = 1 then user_id end)::FLOAT / nullif(count(user_id),0) as session_conversion_rate
from {{ref('mart_ab_test')}}
where (test_group = 'control' AND test_page = 'old_page') OR (test_group = 'treatment' AND test_page = 'new_page')
group by 1
