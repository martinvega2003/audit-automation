# audit-automation

A small end-to-end data pipeline that automates the ingestion, validation, storage, and reporting of retail transaction data.  
The flow simulates a realistic scenario often found in data analysis or audit environments: **Excel (source) → Python (ETL & validations) → SQL (storage) → Excel (clean report for end users)**.

---

## Purpose
This project was built to practice and demonstrate:
- Using Python (`pandas`) to clean, transform, and validate datasets.  
- Persisting structured data in a SQL database (SQLite for the demo).  
- Generating automated Excel reports with summaries and alerts.  
- Following best practices for reproducible pipelines and GitHub documentation.  

It is designed as a **learning project** to showcase skills in Python, SQL, and Excel integration.

---

## Repository Structure

```
audit-automation/
├─ data/
│  ├─ raw_transactions.xlsx        # Input Excel file (example dataset)
│  └─ sample_data_generation.py    # Script to generate sample data with intentional errors
├─ src/
│  ├─ db_schema.sql                # SQL schema for creating tables
│  ├─ ingest.py                    # Reading and validation logic
│  ├─ transform.py                 # Transformations and derived columns
│  ├─ load.py                      # Database insertion (SQLAlchemy)
│  ├─ reports.py                   # Automated Excel report generation
│  └─ run_pipeline.py              # Orchestrator (end-to-end pipeline)
├─ notebooks/
│  └─ exploration.ipynb            # Optional notebook for ad-hoc analysis
├─ README.md
├─ requirements.txt
└─ .gitignore
```

---

## Requirements
- Python 3.9+  

Install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

requirements.txt includes:

```
pandas
openpyxl
xlsxwriter
sqlalchemy
python-dateutil
```

⸻

## Quickstart

1.	Generate sample data:

```
python data/sample_data_generation.py
```

This creates data/raw_transactions.xlsx with some intentional errors (duplicates, invalid dates, negative amounts).

2.	Run the pipeline:

```
python src/run_pipeline.py
```

### Output files:
	•	data/clean_df.pkl → serialized validated dataset
	•	data/alerts.csv → flagged rows with issues
	•	data/transactions.db → SQLite database with transactions table
	•	data/final_report.xlsx → final Excel report with multiple sheets

⸻

### Data Validations

The pipeline applies a series of checks to ensure data quality:
	•	Mandatory fields: transaction_id, date, amount.
	•	Valid date format.
	•	Non-negative transaction amounts.
	•	Duplicate detection (by transaction_id).
	•	Outlier detection (amounts greater than mean + 3*std).

⸻

## Generated Report

The final Excel file contains:
	•	Data_Validated → clean dataset ready for analysis.
	•	Summary_by_Month → aggregated totals per month.
	•	Alerts_Outliers → rows flagged as suspicious or invalid.

This mirrors what an analyst or auditor might need in a real-world workflow.

⸻

## Key Learnings

By completing this project you will practice:
	•	Extracting and validating datasets with Python & pandas.
	•	Designing and using a SQL schema for structured storage.
	•	Exporting multi-sheet Excel reports with summaries and alerts.
	•	Building reproducible, step-by-step pipelines.

⸻

## Future Improvements
	•	Add logging and error handling.
	•	Replace SQLite with PostgreSQL.
	•	Create unit tests for validation rules.
	•	Automate execution with Cron, Airflow, or GitHub Actions.
	•	Export summary data in Parquet/CSV for BI tools.

⸻

## License

This repository is published under the MIT License (add LICENSE if desired).

---
