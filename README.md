# End-to-End AB Testing Experimentation Analytics Platform

## Problem Statement and Business Case
Companies frequently experiment with new product features and user experiences to improve key business outcomes such as customer acquisition, engagement, and conversion. However, making product decisions without a structured experimentation framework can lead to subjective conclusions and costly releases.

This project implements an end-to-end A/B Testing Analytics Engineering platform using a publicly available Kaggle dataset. The experiment compares an existing landing page (Control) with a redesigned landing page (Treatment) to evaluate whether the new experience improves user conversion.

The project demonstrates how raw experimental data can be transformed into trusted business metrics through an analytics engineering workflow. Data is modelled using **dbt**, transformed into analytics-ready marts, and visualized in **Power BI** to provide stakeholders with actionable insights.

The dashboards answers key business questions including:
- Does the new landing page improve conversion rates?
- What is the absolute and relative lift between the two variants?
- How was traffic allocated across the experiment?
- Were there any data quality issues that could affect the validity of the experiment?
- Based on the experimental results, should the new landing page be rolled out?

## Project Objectives
- Build a production-style analytics engineering pipeline for A/B testing data.
- Transform raw experiment data into analytics-ready dimensional models using dbt.
- Calculate standardized A/B testing metrics, including conversion rate, traffic allocation, and experiment lift.
- Develop an executive Power BI dashboard that communicates experiment outcomes and business recommendations.
- Demonstrate analytics engineering best practices, including documentation, data quality validation, and reproducible transformations.

## Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Data Source | [E-Commerce A/B Testing Dataset (Kaggle)](https://www.kaggle.com/datasets/ahmedmohameddawoud/ecommerce-ab-testing) | Source experiment data |
| Local Analytics Database | DuckDB | Data ingestion and local analytical processing |
| Data Warehouse | Snowflake | Central analytical data warehouse |
| Transformation | dbt Core | Analytics engineering and dimensional modelling |
| Version Control | Git & GitHub | Source code management |
| Visualization | Power BI | Executive dashboard and business reporting |

## Data Model

The is section of the document focuses **exclusively on the mart layer** of the data model. The project follows a medallion architecture namely
bronze, silver and the mart layer. A comprehensive description of the data model can be found in the [data dictionary documentation](docs/data_dictionary.pdf).

| Table | Type | Grain | Approx. Rows | Purpose |
|-------|------------|---------|---------| ---------|
| mart_ab_test | Fact |One per user session | ~295k | Base fact table for experiment analysis |
| mart_countries | Mart | One record per user  | ~290k | User distribution by country | 
| mart_country_performance | Mart | One record per distinct registered country | 3 | Conversion metrics by country |
| mart_experiment_summary | Mart | One record per test group  | 2 | Executive A/B testing KPIs |
| mart_high_level_summary | Mart | One summary record | 1 | Overall experiment summary |
| mart_session_analysis | Mart | One record per duration bucket  | 4 | Session duration analysis |

---
## BI Layer

This project uses Power BI as a visualisation layer however, Power BI is not connected to Snowflake to reduce unneccessary complexity.

The 6 mart tables are downloaded from snowflake in CSV format and loaded to Power BI. Additionally, only the pre-aggregated mart tables are
connected to at the BI Layer

## Dashboard Review

### Executive Dashboard

[Screenshot]

### Dashboard

[Screenshot]

### Dashboard

[Screenshot]

---

## Key Skills Demonstrated

- Analytics Engineering
- Product Analytics
- Data Modeling
- SQL
- Python
- Snowflake
- dbt
- Power BI
- AB Testing

---

## Authour
**Ajibola Komolafe** — Analytics Engineer | Data Analyst
- [LinkedIn](https://www.linkedin.com/in/ajibola-komo/) 
- [GitHub](https://github.com/ajibola-komo/)
- [Kaggle](https://www.kaggle.com/ajibsss)