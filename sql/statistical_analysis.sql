CREATE OR REPLACE TABLE mart_statistical_summary (
    total_control_sessions      BIGINT,
    total_treatment_sessions    BIGINT,

    control_conversion_rate     DECIMAL(10,6),
    treatment_conversion_rate   DECIMAL(10,6),

    absolute_lift               DECIMAL(10,6),
    relative_lift               DECIMAL(10,6),

    z_statistic                 DECIMAL(10,4),
    p_value                     DECIMAL(10,6),

    ci_lower                    DECIMAL(12,10),
    ci_upper                    DECIMAL(12,10),

    is_significant              BOOLEAN
);