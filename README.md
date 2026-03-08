# Material Master Data Quality (Python)

This project analyzes material master data to identify common data quality issues in ERP-like datasets.

It demonstrates a simple data quality pipeline using Python and pandas to detect incomplete or inconsistent material master records.

## Tech Stack

- Python
- pandas

## Project Overview

The project is based on a synthetic material master dataset structured like a typical ERP export.

The analysis focuses on identifying common master data quality issues such as:

- negative stock values
- missing material descriptions
- missing units of measure
- missing lead times
- duplicate material IDs

## Python Data Quality Layer

Several validation checks were implemented to transform the raw dataset into structured data quality reports.

The implemented checks include:

- negative stock detection
- missing material descriptions
- missing base units
- missing lead times
- duplicate material IDs

These checks simulate typical validation logic used in ERP-based inventory and supply chain systems.

## Architecture

Raw material master data is stored as a CSV dataset.

Python scripts load the dataset using pandas and apply a set of validation checks.

Detected issues are classified and written into structured output reports.

Workflow:

CSV Dataset → Python (pandas) → Data Quality Checks → Issue Classification → Data Quality Reports

## Output

The pipeline generates two output files:

- `dq_report.csv` – detailed list of material records with detected issues
- `dq_summary.csv` – aggregated summary of issue types

Example output structure:

| material_id | issue |
|-------------|------|
| MAT-1006 | negative_stock |
| MAT-1011 | missing_description |
| MAT-1009 | missing_base_unit |
| MAT-1007 | missing_lead_time |

## Repository Structure

```
material-master-data-quality-python
│
├── data/       synthetic material master dataset
├── src/        Python scripts for loading, validation, and reporting
├── output/     generated data quality reports
├── images/     optional visual documentation
├── README.md
└── requirements.txt
```

## Goal

The goal of this project is to demonstrate how Python and pandas can be used to build a practical data quality validation pipeline for ERP material master datasets.