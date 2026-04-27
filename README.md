# Vendor-lookup

FastAPI project for intelligent vendor name matching using preprocessing, TF-IDF, cosine similarity, and fuzzy matching.

Setup

pip install -r requirements.txt

Run Project

python -m uvicorn main:app --reload

API URLs

•⁠  ⁠Home: http://127.0.0.1:8000/
•⁠  ⁠Docs: http://127.0.0.1:8000/docs

Main Endpoint

POST /match-vendor

Request Body:

{
  "vendor_name": "infy"
}

Data File

Keep vendor master file here:

data/vendors.xlsx