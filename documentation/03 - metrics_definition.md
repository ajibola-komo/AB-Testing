# End-to-End AB Testing Experimentation Analytics Platform - Metrics Definition Documentation

This document defines the business metrics implemented in the A/B Testing Analytics Engineering Platform. For each metric, it provides the business definition, business purpose, calculation formula, SQL implementation, reporting format, and any relevant assumptions to ensure consistent and accurate reporting across the project.

| Metric Name | Business Definition | Calculation | Used In |
| ----------- | ----------- | ----------- | ----------- |
| Total Visitors | Total number of unique users associated with the overall experiment | `COUNT(distinct user_id)` |  Executive Dashboard |
| Total Sessions | Total number of sessions associated with the overall experiement | `COUNT(*)` |  Executive Dashboard |
| Total Conversions | Total number of converted sessions  | `count(case when is_converted = 1 then user_id end)` | Executive Dashboard |
| Session Conversion Rate (SCR) | Rate of conversions based on the total number of sessions | `Total Conversions` / `Total Sessions` | Executive Dashboard |
| Average Session Duration | Average amount of time spent by users on the landing page | `Avg(duration_seconds)` | Executive Dashboard |
| Median Session Duration | Median amount of time spent by users on the landing page | `Median(duration_seconds)` | Executive Dashboard |
| Total Control Conversions | The total number of control group sessions that converted | `COUNT(case when test_group = 'control' and test_page = 'old_page' and is_converted = 1 then user_id end)` | Executive Dashboard |
| Total Treatment Conversions | The total number of treatment group sessions that converted | `COUNT(case when test_group = 'treatment' and test_page = 'new_page' and is_converted = 1 then user_id end)` | Executive Dashboard |
| Control Conversion Rate (CCR) | Rate of conversions from the control group i.e. the old page | `Total Control Conversions` / `Total Control Sessions` | Executive Dashboard |
| Treatment Conversion Rate (TCR) | Rate of conversions from the treatment group i.e. the new page | `Total Treatment Conversions` / `Total Treatment Conversions` | Executive Dashboard |
| Relative Lift | Percentage improvement or decline of the treatment group versus the control group | (`Treatment Conversion Rate` - `Control Conversion Rate`) / `Control Conversion Rate` | Executive Dashboard |
| Absolute Lift | Difference between the treatment and control conversion rates | (`Treatment Conversion Rate` - `Control Conversion Rate`) | Executive Dashboard |
| Total Control Sessions | The total number of control group sessions | `count(case when test_group = 'control' and test_page = 'old_page' then user_id end)` | Executive Dashboard |
| Total Treatment Sessions | The total number of treatment group sessions | `count(case when test_group = 'treatment' and test_page = 'new_page' then user_id end)` | Executive Dashboard |
| Control Traffic Allocation | Percentage of all experiment sessions assigned to the control group. | `Total Control Sessions` / `Total Sessions` | Executive Dashboard |
| Treatment Traffic Allocation | Percentage of all experiment sessions assigned to the Treatment group. | `Total Treatment Sessions` / `Total Sessions` | Executive Dashboard |

## Assumptions

- Conversion rates are calculated at the session level.
- Only valid experiment assignments are included:
  - Control → Old Page
  - Treatment → New Page
- Sessions with mismatched experiment assignments are excluded from KPI calculations.
- Relative Lift is calculated relative to the Control Conversion Rate.
- Traffic Allocation is based on total experiment sessions.

## Authour
**Ajibola Komolafe** — Analytics Engineer | Data Analyst
- [LinkedIn](https://www.linkedin.com/in/ajibola-komo/) 
- [GitHub](https://github.com/ajibola-komo/)
- [Kaggle](https://www.kaggle.com/ajibsss)