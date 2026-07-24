# End-to-End AB Testing Experimentation Analytics Platform

## Problem Statement and Business Case
Companies frequently experiment with new product features and user experiences to improve key business outcomes such as customer acquisition, engagement, and conversion. However, making product decisions without a structured experimentation framework can lead to subjective conclusions and costly releases.

This project implements an end-to-end A/B Testing Analytics Engineering platform using a publicly available Kaggle dataset. The experiment compares an existing landing page (Control) with a redesigned landing page (Treatment) to evaluate whether the new experience improves user conversion.

The project demonstrates how raw experimental data can be transformed into trusted business metrics through an analytics engineering workflow. Data is modelled using dbt, transformed into analytics-ready marts, and visualized in Power BI to provide stakeholders with actionable insights.

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

## Authour
**Ajibola Komolafe** — Analytics Engineer | Data Analyst
- [LinkedIn](https://www.linkedin.com/in/ajibola-komo/) 
- [GitHub](https://github.com/ajibola-komo/)
- [Kaggle](https://www.kaggle.com/ajibsss)