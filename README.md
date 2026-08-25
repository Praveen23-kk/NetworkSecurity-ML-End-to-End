# Network Security ML — End-to-End Phishing Detection

## Overview
Detect phishing (malicious) network entries using an end-to-end Python pipeline. This project includes data ingestion from MongoDB, data validation, data transformation, and model training components. It is intended for researchers and engineers building or evaluating phishing-detection machine learning flows.

## Features
- **Dataset Included:** `Network_Data/phisingData.csv`
- **Data Schema:** Schema and column definitions located in `data_schema/schema.yaml`
- **Data Pushing:** Tools to convert CSV to JSON and push to a MongoDB cluster (`push_data.py`)
- **ML Pipeline:** Code structured modularly under the `networksecurity/` package.
- **Pipeline Components:**
  - Data Ingestion
  - Data Validation
  - Data Transformation
  - Model Training
- **MongoDB Connectivity:** Quick test available via `test_mongodb.py`

---

## Tech Stack
- **Language:** Python (3.8+)
- **Data Manipulation:** pandas, numpy
- **Database:** MongoDB (via pymongo)
- **Machine Learning:** scikit-learn
- **Configuration & Utils:** python-dotenv, pyyaml, dill, certifi

For full packaging dependencies, please refer to `requirements.txt` and `setup.py`.

---

## Repository Layout
```text
ML_Project_v2/
├── networksecurity/               # Main package for ML Pipeline
│   ├── components/                # Pipeline components (Ingestion, Validation, Transformation, Training)
│   ├── constant/                  # Constant values
│   ├── entity/                    # Configuration and Artifact entity definitions
│   ├── exception/                 # Custom exception handling
│   ├── logging/                   # Custom logging configuration
│   ├── pipline/                   # Pipeline definitions
│   └── utils/                     # Utility scripts and helpers
├── Network_Data/                  # Raw dataset directory
│   └── phisingData.csv            # Phishing network dataset
├── data_schema/                   # Data schema configurations
│   └── schema.yaml                # Schema rules for data validation
├── notebooks/                     # Jupyter notebooks for EDA and experiments
├── push_data.py                   # Script to push local CSV data to MongoDB
├── main.py                        # Entry point to trigger the ML pipeline
├── test_mongodb.py                # Script to test MongoDB connectivity
├── requirements.txt               # Required Python dependencies
├── setup.py                       # Packaging script
├── Dockerfile                     # Docker configuration
└── .env                           # Environment variables (MongoDB URL, etc.)
```

---

## Getting Started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd ML_Project_v2
```

### 2. Create a Virtual Environment and Install Dependencies
```bash
python -m venv venv
# On Windows use: venv\Scripts\activate
# On Unix use: source venv/bin/activate
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory (if not already present) and add your MongoDB connection string:
```
MONGO_DB_URL="your_mongodb_connection_string_here"
```

### 4. Push Data to MongoDB
To initialize your MongoDB with the provided dataset:
```bash
python push_data.py
```

### 5. Run the Pipeline
To trigger the end-to-end ML pipeline (Ingestion, Validation, Transformation, etc.):
```bash
python main.py
```
