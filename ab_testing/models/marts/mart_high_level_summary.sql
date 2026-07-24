select 

-- Total Sessions
count(*) as total_sessions,

-- Control Conversion Rate
count(case when is_converted = 1 and test_group = 'control' and test_page = 'old_page' then user_id end)::FLOAT /
nullif(count(case when test_group = 'control' and test_page = 'old_page' then user_id end),0) as control_conversion_rate,

-- Treatment Conversion Rate
count(case when is_converted = 1 and test_group = 'treatment' and test_page = 'new_page' then user_id end)::FLOAT /
nullif(count(case when test_group = 'treatment' and test_page = 'new_page' then user_id end),0) as treatment_conversion_rate,

-- Relative Lift
(
count(case when is_converted = 1 and test_group = 'treatment' and test_page = 'new_page' then user_id end)::FLOAT /
nullif(count(case when test_group = 'treatment' and test_page = 'new_page' then user_id end),0) 
- 
count(case when is_converted = 1 and test_group = 'control' and test_page = 'old_page' then user_id end)::FLOAT /
nullif(count(case when test_group = 'control' and test_page = 'old_page' then user_id end),0)
) 
/ 
(count(case when is_converted = 1 and test_group = 'control' and test_page = 'old_page' then user_id end)::FLOAT /
nullif(count(case when test_group = 'control' and test_page = 'old_page' then user_id end),0)) as relative_lift,

-- Absolute Lift
(
count(case when is_converted = 1 and test_group = 'treatment' and test_page = 'new_page' then user_id end)::FLOAT /
nullif(count(case when test_group = 'treatment' and test_page = 'new_page' then user_id end),0) 
- 
count(case when is_converted = 1 and test_group = 'control' and test_page = 'old_page' then user_id end)::FLOAT /
nullif(count(case when test_group = 'control' and test_page = 'old_page' then user_id end),0)
) as absolute_lift,

count(case when test_group = 'control' and test_page = 'old_page' then user_id end)::FLOAT/
nullif(count(user_id),0) as control_traffic_allocation,

count(case when test_group = 'treatment' and test_page = 'new_page' then user_id end)::FLOAT/
nullif(count(user_id),0) as treatment_traffic_allocation

from {{ref('mart_ab_test')}}


