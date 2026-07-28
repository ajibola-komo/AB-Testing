select 
    id as user_id,
    SPLIT_PART(event_time, ':', 1)::FLOAT * 60 + SPLIT_PART(event_time, ':', 2)::FLOAT AS duration_seconds,
    con_treat as test_group,
    page as test_page,
    converted as is_converted
from {{source('bronze', 'ab_test')}} where id is not null and id in (
            select user_id from {{ref('silver_valid_ab_users')}}
)