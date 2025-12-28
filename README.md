# AI-Enabled Misinformation as a Cybersecurity Threat to England’s Financial Sector (2020–2024)

This repository contains all supporting materials for the dissertation:
**“AI-Enabled Misinformation as a Cybersecurity Threat to England’s Financial Sector (2020–2024)”**.

It includes:
- A simulated GDELT-style dataset of 1,100 misinformation events
- Python scripts for dataset generation and analysis
- Documentation and schema files
- Visualisations generated during the study
- Jupyter notebooks for replication

---

## 📌 Project Overview

Financial institutions in England are increasingly targeted by AI-enabled misinformation, including deepfakes, synthetic regulatory announcements, and false insolvency rumours.  
Due to a lack of publicly available datasets, a realistic simulated dataset was created based on:

- GDELT-style event coding  
- Patterns from the Bank of England Systemic Risk Survey  
- Misinformation typologies from academic literature  

This repository allows anyone to **replicate the analysis**, **inspect the dataset**, or **extend the study**.

---

## 📂 Repository Structure

financial-misinformation-analysis-2020-2024/
│
├── data/
│ ├── financial_misinformation_2020_2024_full_dataset.csv
│ └── sample_rows_preview.csv
│
├── scripts/
│ ├── generate_dataset.py
│ ├── analysis_script.py
│ └── utils.py
│ └── analysis_notebook.ipynb
│
├── dataset_schema.md


---

## 📊 Dataset Description

A GDELT-style dataset with the following key fields:

| Column | Description |
|--------|------------|
| event_id | Unique numerical identifier |
| date | Event date |
| year / month | Extracted temporal dimensions |
| city | English city where the misinformation was attributed |
| latitude / longitude | Geolocation |
| narrative_type | Six misinformation categories |
| tone_score | Sentiment score (-10 to +10) |
| mentions | Approx amplification level (5–35) |
| description | Brief explanation |
| sector_reference | Always “Financial Sector” |

Full schema is available in `docs/dataset_schema.md`.

---

## 🧪 Scripts Included

### 1️⃣ **generate_dataset.py**
Creates the full 1,100-row misinformation dataset.

### 2️⃣ **analysis_script.py**
Runs all descriptive and visual analyses including:

- Yearly event trends
- City-level distribution
- Narrative classification analysis
- Sentiment analysis
- Amplification modelling  

Visuals export to `/docs/figures/`.

---

## ▶️ How to Run

1. Clone the repository:

2. Install required packages:

3. Generate the dataset:

4. Run the analysis:

5. View notebooks:
Open `analysis_notebook.ipynb` in Jupyter.

---

## 🛡️ Ethical Statement

This project uses **fully simulated data**.  
No real misinformation content or real institutions are harmed or identified.  
All outputs are for academic research and methodological demonstration only.

---

## 📄 License

MIT License (included in `LICENSE` file).

---

## 📬 Contact

For academic questions related to this project, contact:

**Veera**  
MSc Business Analytics Dissertation Project

