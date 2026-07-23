select id as user_id, country from {{source('bronze', 'countries')}}
where id is not null