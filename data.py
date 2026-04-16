"""
Run this once to generate a sample vendors.xlsx for testing.
Usage: python create_sample_data.py
"""
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

data = {
    "vendor_code": [
        f"V{1000+i}" for i in range(1, 101)
    ],
    "vendor_name": [
        "Infosys Technologies Ltd",
        "Infosys BPO Ltd",
        "Tata Consultancy Services",
        "Tata Motors Ltd",
        "Wipro Limited",
        "HCL Technologies",
        "ABC Traders Pvt Ltd",
        "ABC Trading Company",
        "Reliance Industries Ltd",
        "Reliance Retail Ltd",

        "Tech Mahindra Ltd",
        "Larsen & Toubro Ltd",
        "Adani Enterprises Ltd",
        "Adani Ports and SEZ Ltd",
        "Bharti Airtel Ltd",
        "Vodafone Idea Ltd",
        "Hindustan Unilever Ltd",
        "ITC Limited",
        "Asian Paints Ltd",
        "Maruti Suzuki India Ltd",

        "Hero MotoCorp Ltd",
        "Bajaj Auto Ltd",
        "Nestle India Ltd",
        "Britannia Industries Ltd",
        "Dabur India Ltd",
        "Godrej Consumer Products",
        "Zomato Ltd",
        "Swiggy Pvt Ltd",
        "Flipkart Internet Pvt Ltd",
        "Amazon Seller Services",

        "Paytm Payments Bank",
        "PhonePe Pvt Ltd",
        "Google India Pvt Ltd",
        "Microsoft India Pvt Ltd",
        "IBM India Pvt Ltd",
        "Accenture Solutions Pvt Ltd",
        "Capgemini Technology Services",
        "Cognizant Technology Solutions",
        "Oracle India Pvt Ltd",
        "SAP Labs India",

        "Dell India Pvt Ltd",
        "HP India Sales Pvt Ltd",
        "Lenovo India Pvt Ltd",
        "Asus India Pvt Ltd",
        "Acer India Pvt Ltd",
        "Redington India Ltd",
        "Ingram Micro India Ltd",
        "Tech Data India Ltd",
        "Reliance Jio Infocomm Ltd",
        "Jio Platforms Ltd",

        "Infosys Consulting India",
        "TCS Digital Solutions",
        "Wipro Infrastructure Engineering",
        "HCL Infosystems Ltd",
        "Mindtree Ltd",
        "Mphasis Ltd",
        "L&T Infotech Ltd",
        "Persistent Systems Ltd",
        "Hexaware Technologies Ltd",
        "NIIT Technologies Ltd",

        "Blue Dart Express Ltd",
        "Delhivery Pvt Ltd",
        "Ecom Express Pvt Ltd",
        "DTDC Courier & Cargo Ltd",
        "India Post Logistics",
        "Gati Ltd",
        "VRL Logistics Ltd",
        "TCI Express Ltd",
        "Mahindra Logistics Ltd",
        "Allcargo Logistics Ltd",

        "Reliance Digital Retail",
        "Croma Retail Ltd",
        "Vijay Sales Pvt Ltd",
        "Poorvika Mobiles Pvt Ltd",
        "Sangeetha Mobiles Pvt Ltd",
        "Big Bazaar Retail Ltd",
        "Dmart Retail Ltd",
        "Spencer’s Retail Ltd",
        "More Retail Pvt Ltd",
        "Future Retail Ltd",

        "Apollo Hospitals Ltd",
        "Fortis Healthcare Ltd",
        "Max Healthcare Institute",
        "Narayana Health Ltd",
        "Manipal Hospitals Pvt Ltd",
        "Aster DM Healthcare",
        "Medanta Hospitals",
        "Columbia Asia Hospitals",
        "Care Hospitals Group",
        "Global Hospitals Ltd",

        "Byju’s Learning App",
        "Unacademy Pvt Ltd",
        "Vedantu Innovations Pvt Ltd",
        "WhiteHat Jr Pvt Ltd",
        "UpGrad Education Pvt Ltd",
        "Simplilearn Solutions Pvt Ltd",
        "Great Learning Pvt Ltd",
        "Scaler Academy Pvt Ltd",
        "PhysicsWallah Pvt Ltd",
        "Toppr Learning Pvt Ltd"
    ]
}

df = pd.DataFrame(data)
df.to_excel("data/vendors.xlsx", index=False)
print("✅ Sample vendors.xlsx created in data/")