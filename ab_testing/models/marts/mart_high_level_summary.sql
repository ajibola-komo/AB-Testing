with get_metrics as (
    select count(*) as total_sessions,

    count(distinct user_id) as total_visitors,

    count(case when is_converted = 1 then user_id end) as total_conversions,

    avg(duration_seconds) as average_session_duration,

    median(duration_seconds) as median_session_duration,

    count(case when test_group = 'control' and test_page = 'old_page' and is_converted = 1 then user_id end) as total_control_conversions,

    count(case when test_group = 'treatment' and test_page = 'new_page' and is_converted = 1 then user_id end) as total_treatment_conversions,

    count(case when test_group = 'treatment' and test_page = 'new_page' then user_id end) as total_treatment_sessions,

    count(case when test_group = 'control' and test_page = 'old_page' then user_id end) as total_control_sessions

    from {{ref('mart_ab_test')}}

    where (test_group = 'control' and test_page = 'old_page') or (test_group = 'treatment' and test_page = 'new_page')
)

select 

-- Total Sessions
total_sessions,

total_visitors,

total_conversions,

total_conversions / total_sessions as session_conversion_rate,

-- Control Conversion Rate
total_control_conversions::FLOAT / total_control_sessions as control_conversion_rate,

-- Treatment Conversion Rate
total_treatment_conversions::FLOAT / total_treatment_sessions as treatment_conversion_rate,

-- Relative Lift
(
(total_treatment_conversions::FLOAT / total_treatment_sessions)
- 
(total_control_conversions::FLOAT / total_control_sessions) )
/ 
(total_treatment_conversions::FLOAT / total_treatment_sessions)
 as relative_lift,

-- Absolute Lift
((total_treatment_conversions::FLOAT / total_treatment_sessions)
- 
(total_control_conversions::FLOAT / total_control_sessions) ) as absolute_lift,

-- control traffic allocation
total_control_sessions::FLOAT/ total_sessions as control_traffic_allocation,

-- treatment traffic allocation
total_treatment_sessions::FLOAT/ total_sessions as treatment_traffic_allocation,

average_session_duration,

median_session_duration,

from get_metrics


