# Grade Evaluator & Archiver

A Python application that reads a student's course grades from a CSV file, validates the data, calculates their GPA, and determines their final academic standing.

---

## What It Does

- Validates that all scores are between 0 and 100
- Verifies Formative weights sum to 60 and Summative weights sum to 40
- Calculates the weighted final grade and GPA (out of 5.0)
- Determines Pass/Fail status based on 50% minimum in both categories
- Identifies which failed Formative assignment is eligible for resubmission
- - GPA is calculated using the formula: (Total Grade / 100) × 5.0
---

## Files

| File | Description |
|------|-------------|
| `grade-evaluator.py` | Main Python script |
| `organizer.sh` | Shell script to archive grades and reset workspace |
| `grades.csv` | Student grade data |

---

## Prerequisites

- Python 3.x installed
- Bash terminal (Mac/Linux)

---

## How to Run

### Python Script
```bash
cd lab1_etenna-maker
python3 grade-evaluator.py
```
When prompted, type `grades.csv` and press Enter.

### Shell Script
```bash
cd lab1_etenna-maker
bash organizer.sh
```
This archives `grades.csv` with a timestamp, creates a fresh `grades.csv`, and logs the operation to `organizer.log`.

---

## CSV Format
