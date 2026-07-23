-- session level metrics for each test group
select test_group, 
count(distinct user_id) as total_visitors,
count(*) as total_sessions,
count(case when is_converted = 1 then user_id end) as total_conversions,
count(case when is_converted = 1 then user_id end)::FLOAT/nullif(count(user_id),0) as session_conversion_rate,
count(distinct case when is_converted = 1 then user_id end)::FLOAT/nullif(count(distinct user_id),0) as visitor_conversion_rate,
avg(duration_seconds) as average_session_duration,
median(duration_seconds) as median_session_duration
from {{ref('ab_test_mart')}}
WHERE
    (test_group = 'control' AND test_page = 'old_page')
    OR
    (test_group = 'treatment' AND test_page = 'new_page')
group by test_group