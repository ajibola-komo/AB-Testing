select 
case
when duration_seconds < 10 then 'Less than 10 Sec'
when duration_seconds between 10 and 20 then '10 - 20 Sec'
when duration_seconds between 20 and 30 then '20 - 30 Sec'
else 'Over 30 Sec'
end as duration_bucket,
count(distinct user_id) as total_visitors,
count(*) as total_sessions,
count(case when is_converted = 1 then user_id end)::FLOAT / nullif(count(user_id),0) as session_conversion_rate,
count(distinct case when is_converted = 1 then user_id end)::FLOAT / nullif(count(distinct user_id),0) as visitor_conversion_rate
from {{ref('mart_ab_test')}}
where (test_group = 'control' AND test_page = 'old_page')
    OR
    (test_group = 'treatment' AND test_page = 'new_page')
group by duration_bucket
