# Automated Sales Analytics Pipeline

## Overview

An end-to-end data pipeline designed to process raw sales data, store it in a relational database, and enable analytical reporting through a BI tool. The system automates data ingestion, transformation, and loading to support efficient and scalable data analysis.

---

## Problem

Organizations relying on spreadsheet-based workflows face:

* Manual data processing and repetitive tasks
* Data inconsistencies (duplicates, formatting issues)
* Limited scalability for analysis
* Delayed reporting and decision-making

---

## Solution

This project implements an automated ETL pipeline that:

* Extracts raw data from CSV/Excel sources
* Cleans and standardizes the dataset
* Aggregates records to ensure data integrity
* Loads structured data into PostgreSQL using UPSERT logic
* Enables reporting through a connected BI dashboard

---

## Architecture

```
CSV/Excel → Python (ETL) → PostgreSQL → BI Dashboard
                ↑
        Scheduled Execution
```

---

## Tech Stack

* Python (Pandas)
* PostgreSQL
* Power BI
* Windows Task Scheduler

---

## Data Processing

* Column standardization for consistency
* Datetime conversion for temporal analysis
* Duplicate handling via aggregation on business keys
* Missing value handling using default strategies

---

## Database Design

* Structured relational table for sales data
* Composite key: (order_id, product_id)
* UPSERT mechanism for incremental updates

---

## Automation

* Scheduled execution using Windows Task Scheduler
* Ensures periodic data refresh without manual intervention

---

## Outcome

* Streamlined data pipeline
* Improved data quality and consistency
* Reduced manual effort
* Faster and reliable reporting

---

## Repository Structure

```
project/
│
├── dataset/
├── scripts/
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── main.py
├── README.md
└── dashboard.png
```

---

## Usage

1. Update the source CSV file
2. Run the pipeline script (or rely on scheduler)
3. Refresh the BI dashboard

---

## Notes

* Database credentials should be managed securely (use environment variables)
* Designed for batch processing workflows

---

## Dashboard Preview

<p align="center">
  <img src="dashboard.png" width="800"/>
</p>
