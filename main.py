from fastapi import FastAPI
from pydantic import BaseModel
from extractor import load_vendors
from models.matcher import VendorMatcher

app = FastAPI(title="Vendor Lookup API")

matcher = None


class VendorRequest(BaseModel):
    vendor_name: str


def load_matcher():
    global matcher
    vendors = load_vendors()
    matcher = VendorMatcher(vendors)


# Load once at startup
load_matcher()


@app.get("/")
def home():
    return {
        "message": "Vendor API Running",
        "status": "OK"
    }


@app.post("/match-vendor")
def match_vendor(request: VendorRequest):
    return matcher.search(request.vendor_name)


@app.post("/reload-data")
def reload_data():
    load_matcher()
    return {
        "message": "Vendor data reloaded successfully"
    }