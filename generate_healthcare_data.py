"""
Healthcare Supply Chain Financial Data Generator
Mayo Clinic Performance Consulting Analyst Portfolio Project
Generates realistic hospital supply chain data for financial analysis
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_healthcare_scm_data(n_records=100000):
    """
    Generate hospital supply chain procurement and usage data
    Focus on Surgical, Cardiology, Radiology, and GI departments
    """
    print(f"Generating {n_records:,} healthcare supply chain records...")
    
    # Date range: 12 months of data
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    # Mayo Clinic departments (surgical, cardiology, radiology, GI preferred)
    departments = [
        'Cardiology', 'Cardiology', 'Surgery', 'Surgery', 'Surgery',  # Weighted for preference
        'Radiology', 'Radiology', 'GI', 'GI', 'Orthopedics', 
        'Neurology', 'Oncology', 'Emergency', 'ICU', 'General Medicine'
    ]
    
    # Medical supply categories
    categories = {
        'Surgical Instruments': {'cost_range': (500, 5000), 'shelf_life': 1095},  # 3 years
        'Cardiac Implants': {'cost_range': (2000, 15000), 'shelf_life': 730},     # 2 years
        'Radiology Contrast': {'cost_range': (50, 300), 'shelf_life': 180},       # 6 months
        'GI Endoscopy Supplies': {'cost_range': (100, 800), 'shelf_life': 365},   # 1 year
        'Sutures': {'cost_range': (20, 200), 'shelf_life': 1825},                 # 5 years
        'PPE': {'cost_range': (5, 50), 'shelf_life': 365},
        'Pharmaceuticals': {'cost_range': (100, 2000), 'shelf_life': 270},
        'Medical Devices': {'cost_range': (1000, 25000), 'shelf_life': 1095},
        'Lab Supplies': {'cost_range': (30, 500), 'shelf_life': 180},
        'Orthopedic Implants': {'cost_range': (3000, 20000), 'shelf_life': 1095}
    }
    
    vendors = [
        'Medtronic', 'Johnson & Johnson', 'Stryker', 'Boston Scientific', 
        'Abbott', 'Becton Dickinson', 'Cardinal Health', 'McKesson',
        'Fisher Scientific', 'GE Healthcare', 'Siemens', 'Philips'
    ]
    
    data = []
    
    for i in range(n_records):
        # Generate date
        days_offset = random.randint(0, 364)
        date = start_date + timedelta(days=days_offset)
        
        # Select attributes
        dept = random.choice(departments)
        category = random.choice(list(categories.keys()))
        vendor = random.choice(vendors)
        
        # Get category details
        cat_info = categories[category]
        unit_cost = round(random.uniform(cat_info['cost_range'][0], cat_info['cost_range'][1]), 2)
        
        # Quantity and usage patterns (higher for surgery/cardiology)
        if dept in ['Surgery', 'Cardiology']:
            qty_ordered = random.randint(50, 500)
        elif dept in ['Emergency', 'ICU']:
            qty_ordered = random.randint(100, 1000)
        else:
            qty_ordered = random.randint(20, 200)
        
        # Simulate usage vs waste (expired/damaged)
        usage_rate = random.uniform(0.75, 0.98)  # 75-98% usage
        qty_used = int(qty_ordered * usage_rate)
        qty_wasted = qty_ordered - qty_used
        
        # Financial calculations
        total_cost = round(qty_ordered * unit_cost, 2)
        used_value = round(qty_used * unit_cost, 2)
        wasted_value = round(qty_wasted * unit_cost, 2)
        
        # GL Account mapping (healthcare accounting)
        gl_accounts = {
            'Surgical Instruments': '6100-01',
            'Cardiac Implants': '6100-02',
            'Radiology Contrast': '6200-01',
            'GI Endoscopy Supplies': '6300-01',
            'Sutures': '6100-03',
            'PPE': '6400-01',
            'Pharmaceuticals': '6500-01',
            'Medical Devices': '6600-01',
            'Lab Supplies': '6700-01',
            'Orthopedic Implants': '6100-04'
        }
        
        gl_account = gl_accounts[category]
        
        # Variance analysis (some items have price variances)
        standard_cost = unit_cost * random.uniform(0.95, 1.05)
        price_variance = round((unit_cost - standard_cost) * qty_ordered, 2)
        
        # Inventory metrics
        days_in_inventory = random.randint(15, 180)
        carrying_cost_rate = 0.25  # 25% annual carrying cost
        carrying_cost = round((total_cost * carrying_cost_rate) * (days_in_inventory / 365), 2)
        
        data.append({
            'Transaction_ID': f"SCM_{i:07d}",
            'Date': date.strftime('%Y-%m-%d'),
            'Department': dept,
            'Category': category,
            'Vendor': vendor,
            'GL_Account': gl_account,
            'Unit_Cost': unit_cost,
            'Qty_Ordered': qty_ordered,
            'Qty_Used': qty_used,
            'Qty_Wasted': qty_wasted,
            'Total_Cost': total_cost,
            'Used_Value': used_value,
            'Wasted_Value': wasted_value,
            'Price_Variance': price_variance,
            'Days_In_Inventory': days_in_inventory,
            'Carrying_Cost': carrying_cost,
            'Month': date.month,
            'Quarter': (date.month - 1) // 3 + 1
        })
        
        if (i+1) % 20000 == 0:
            print(f"Generated {i+1:,} records...")
    
    return pd.DataFrame(data)

# Generate data
df = generate_healthcare_scm_data(100000)

# Save to CSV
df.to_csv('data/healthcare_scm_data.csv', index=False)
print(f"\n✓ Dataset created: {len(df):,} records")
print(f"✓ File saved: data/healthcare_scm_data.csv")
print(f"✓ Total Spend Analyzed: ${df['Total_Cost'].sum():,.2f}")
print(f"✓ Total Waste Identified: ${df['Wasted_Value'].sum():,.2f}")
print(f"✓ Carrying Costs: ${df['Carrying_Cost'].sum():,.2f}")

# Generate summary statistics
print("\n" + "="*60)
print("HEALTHCARE SCM FINANCIAL SUMMARY")
print("="*60)
print(f"Departments: {df['Department'].nunique()}")
print(f"Categories: {df['Category'].nunique()}")
print(f"Vendors: {df['Vendor'].nunique()}")
print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")
print("\nTop 5 Cost Categories:")
print(df.groupby('Category')['Total_Cost'].sum().sort_values(ascending=False).head().to_string())
print("\nWaste by Department:")
print(df.groupby('Department')['Wasted_Value'].sum().sort_values(ascending=False).head().to_string())
