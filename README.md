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

---

## Recent Changes
- **Model Training wired into the pipeline:** `main.py` now runs `ModelTrainer` after Data Transformation and prints the model trainer artifact.
- **Model selection:** `ModelTrainer.train_model` compares Random Forest, Decision Tree, Gradient Boosting, Logistic Regression and AdaBoost using hyperparameter grids, picks the best model by score, and saves it (together with the preprocessor, as `NetworkModel`) to the trained-model path.
- **Metrics:** train and test classification metrics are computed for the best model and returned in `ModelTrainerArtifact`.
- **`evaluate_models` utility:** new helper in `utils/main_utils/utils.py` that runs `GridSearchCV` (cv=3) per model and reports the test score.
- **`ModelTrainerConfig` fixed:** corrected parameter and constant names (`training_pipeline_config`, `artifact_dir`, `MODEL_TRAINER_DIR_NAME`, etc.) and the `overfitting_underfitting_threshold` spelling.
- **Data ingestion fallback:** if MongoDB is unreachable (5s timeout), ingestion falls back to reading `Network_Data/phisingData.csv`.
- **Logging:** added `networksecurity/logging/logger.py`.

---

## Workflow (What We Did So Far)
```text
MongoDB / CSV  ->  Data Ingestion  ->  Data Validation  ->  Data Transformation  ->  Model Training  ->  Saved Model
(push_data.py)     (train/test split)   (schema.yaml check)   (preprocessor + .npy)    (GridSearchCV)      (model.pkl)
```
1. **Data push:** `push_data.py` converts `Network_Data/phisingData.csv` to JSON and loads it into MongoDB.
2. **Data Ingestion:** reads the collection from MongoDB (falls back to the local CSV if unreachable), drops `_id`, and splits into train/test files.
3. **Data Validation:** checks the data against `data_schema/schema.yaml` (columns, drift) and produces a validation artifact.
4. **Data Transformation:** builds and saves the preprocessing object and writes transformed train/test arrays as `.npy` files.
5. **Model Training:** tries several classifiers with grid search, selects the best, computes train/test metrics, and saves the model together with the preprocessor as `NetworkModel`.
6. **Orchestration:** `main.py` runs all stages in order, with custom logging and `NetworkSecurityException` for error reporting.

## Tools Used
- **Claude (Claude Code)** and **Antigravity CLI** were used for bug fixing and error handling during development.
