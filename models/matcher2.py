from extractor2 import load_line_items

def dispatch_vendor_details(vendor_code: str) -> dict:
    all_items  = load_line_items()
    line_items = [item for item in all_items if item["vendor_code"] == vendor_code]

    if not line_items:
        return {"success": False, "error": f"No data found for vendor_code: {vendor_code}"}

    payload = {
        "vendor_code":       vendor_code,
        "vendor_name":       line_items[0]["vendor_name"],
        "company_code":      line_items[0]["company_code"],
        "business_place":    line_items[0]["business_place"],
        "section_code":      line_items[0]["section_code"],
        "total_invoice_amt": line_items[0]["total_invoice_amt"],
        "line_items": [
            {
                "line_item":                 item["line_item"],
                "material_code":             item["material_code"],
                "description":               item["description"],
                "service_code":              item["service_code"],
                "ocr_line_item_description": item["ocr_line_item_description"],
                "line_amt":                  item["line_amt"],
                "cost_centre":               item["cost_centre"],
                "gl_code":                   item["gl_code"],
            }
            for item in line_items
        ]
    }

    return payload
