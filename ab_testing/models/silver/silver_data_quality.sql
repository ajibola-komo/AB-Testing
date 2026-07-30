select

    COUNT(case when(con_treat = 'control' and page = 'new_page') or 
    (con_treat = 'treatment' AND page = 'old_page') THEN 1 END)::FLOAT / COUNT(*) as invalid_assignment_rate,

    1 - ((COUNT(case when(con_treat = 'control' and page = 'new_page') or 
    (con_treat = 'treatment' AND page = 'old_page') THEN 1 END))::FLOAT / COUNT(*)) as valid_assignment_rate


from {{source('bronze','ab_test')}}