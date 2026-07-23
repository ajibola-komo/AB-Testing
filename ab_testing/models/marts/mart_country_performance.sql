select s.country, count(distinct t.user_id) as total_visitors,
count(t.user_id) as total_sessions,
count(case when t.is_converted = 1 then t.user_id end) as total_conversions,
count(case when t.is_converted = 1 then t.user_id end) / nullif(count(t.user_id),0) as session_conversion_rate,
count(distinct case when t.is_converted = 1 then t.user_id end) / nullif(count(distinct t.user_id),0) as visitor_conversion_rate,
avg(t.duration_seconds) as average_session_duration
from {{ref('silver_countries')}} s inner join {{ref('silver_ab_test')}} t
on s.user_id = t.user_id
where (t.test_group = 'control' and test_page = 'old_page') or (t.test_group = 'treatment' and test_page = 'new_page')
group by s.country