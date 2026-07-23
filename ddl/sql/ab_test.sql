create or replace table ab_test(
    id int,
    event_time varchar(10),
    con_treat varchar(50),
    page varchar(50),
    converted smallint
);