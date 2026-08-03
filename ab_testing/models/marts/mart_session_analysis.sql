select 
CASE
    WHEN duration_seconds < 10 AND duration_seconds <= 60 THEN 'Less than 1 Min'
    WHEN duration_seconds > 60 AND duration_seconds <= 300 THEN '1 - 5 Min'
    WHEN duration_seconds > 300 AND duration_seconds <= 600 THEN '5 - 10 Min'
    ELSE '10+ Min'
END as duration_bucket,
count(distinct user_id) as total_visitors,
count(*) as total_sessions,
count(case when is_converted = 1 then user_id end) as total_conversions,
count(case when is_converted = 1 then user_id end)::FLOAT / nullif(count(*),0) as session_conversion_rate
from {{ref('silver_ab_test')}}
group by 1
