select

    COUNT(case when(test_group = 'control' and test_page = 'new_page') or 
    (test_group = 'treatment' AND test_page = 'old_page') THEN 1 END)::FLOAT / COUNT(*) as invalid_assignment_rate,

    1 - ((COUNT(case when(test_group = 'control' and test_page = 'new_page') or 
    (test_group = 'treatment' AND test_page = 'old_page') THEN 1 END))::FLOAT / COUNT(*)) as valid_assignment_rate


from {{ref('mart_ab_test')}}