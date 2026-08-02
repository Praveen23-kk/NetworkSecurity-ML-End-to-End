# Network Security ML — End-to-End Phishing Detection

One-line summary
Detect phishing (malicious) network entries using an end-to-end Python pipeline: ingestion, validation, storage and (projected) training/evaluation components. Intended for researchers and engineers building or evaluating phishing-detection ML flows.

## Features
- CSV dataset included (Network_Data/phisingData.csv)
- Data schema and column definitions (data_schema/schema.yaml)
- Tools to convert CSV → JSON and push to MongoDB (push_data.py)
- Basic data ingestion and validation entry point (main.py)
- Package skeleton and modular code under `networksecurity/` for pipeline, utils and components
- Quick MongoDB connectivity test (test_mongodb.py)

---

## Stack
- Language: Python (100%)
- Runtime: CPython 3.8+ (assumed)
- Notable libraries (observed in code):
  - pandas, numpy — data loading/transformation
  - pymongo — load/store to MongoDB
  - certifi — TLS certificate bundle for MongoDB connections
  - (project modules) networksecurity.* — ingestion, validation, pipeline components

See `requirements.txt` / `setup.py` for full packaging dependencies.

---

## Repository layout (top-level)
