from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from extractor import load_vendors
from models.matcher import VendorMatcher
from models.matcher2 import dispatch_vendor_details


app = FastAPI(title="Vendor Lookup API")

matcher = None


class VendorRequest(BaseModel):
    vendor_name: str


class VendorDetailsRequest(BaseModel):
    vendor_code: str


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


@app.post("/vendor-details")
def vendor_details(request: VendorDetailsRequest):
    """
    Payload:  { "vendor_code": "V1001" }
    """
    if not request.vendor_code:
        raise HTTPException(status_code=400, detail="vendor_code is required.")
 
    result = dispatch_vendor_details(request.vendor_code)
 
    if not result.get("success", True) and "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
 
    return result
 
 
@app.post("/reload-data")
def reload_data():
    load_matcher()
    return {"message": "Vendor data reloaded successfully"}