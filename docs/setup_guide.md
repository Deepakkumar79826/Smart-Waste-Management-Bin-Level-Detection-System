# Setup Guide

## Step 1

Install Python 3.10+

Verify:

python --version

---

## Step 2

Install dependencies:

pip install -r requirements.txt

---

## Step 3

Create required folders:

data/

outputs/

---

## Step 4

Run Monitoring System

python main.py

---

## Step 5

Open Dashboard

streamlit run dashboard/app.py

---

## Step 6

View Outputs

CSV Logs:

data/waste_log.csv

PDF Reports:

outputs/waste_report.pdf

Dashboard:

outputs/dashboard.html

---

## Troubleshooting

### ModuleNotFoundError

Create:

python_simulation/**init**.py

### Missing CSV

Run:

python main.py

### Streamlit Error

Install:

pip install streamlit

### Plotly Error

Install:

pip install plotly
