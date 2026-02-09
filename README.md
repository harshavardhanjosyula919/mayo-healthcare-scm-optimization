# Healthcare Supply Chain Financial Optimization
**Mayo Clinic Performance Consulting Analyst Portfolio Project**

![Healthcare SCM Dashboard](assets/healthcare_scm_dashboard.png)

## Overview
Strategic financial analysis of healthcare supply chain operations identifying **$2.8M in cost reduction opportunities** through waste elimination, inventory optimization, and vendor consolidation.

**Context:** Mayo Clinic Performance Consulting Analyst role focusing on surgical, cardiology, radiology, and GI supply chain financial management.

## Business Problem
Hospital supply chain showing:
- **18.5% waste rate** (expired/unused supplies) = $1.9M annual loss
- **Excess inventory carrying costs** = $890K annually
- **Price variances** across GL accounts requiring reconciliation
- **Vendor performance gaps** in high-cost surgical and cardiac categories

## Key Findings

| Metric | Value | Impact |
|--------|-------|--------|
| Total Annual Spend | $156.4M | Baseline |
| Supply Waste | $18.9M (12.1%) | **Cost Reduction Target** |
| Carrying Costs | $890K | **Inventory Optimization** |
| Price Variances | $450K | **GL Reconciliation** |
| **Total Opportunity** | **$2.8M** | **18% Improvement** |

## Department Analysis (Priority Areas)
- **Surgery**: $42M spend, 14.2% waste rate (highest volume)
- **Cardiology**: $38M spend, 11.8% waste rate (implant costs)
- **Radiology**: $22M spend, 9.4% waste rate (contrast media)
- **GI**: $18M spend, 13.1% waste rate (endoscopy supplies)

## Technical Implementation

### Files
- `generate_healthcare_data.py` - Creates realistic hospital SCM data (100K records)
- `financial_analysis.py` - Cost reduction analysis and visualizations
- `sql_queries.sql` - GL reconciliation and financial reporting queries
- `data/` - Processed datasets and summary exports

### Tools Used
- **SQL:** Complex queries for GL reconciliation, variance analysis
- **Python:** Pandas for cost analysis, Matplotlib/Seaborn for executive dashboards
- **Excel:** Financial modeling and variance reporting
- **Financial Analysis:** Inventory carrying cost models, waste reduction strategies

## Strategic Recommendations

### 1. Vendor Consolidation ($1.2M savings)
- Target top 3 underperforming vendors (waste rates &gt;20%)
- Renegotiate contracts with standardized unit pricing
- Implement vendor-managed inventory (VMI) for high-cost items

### 2. Inventory Optimization ($890K savings)
- Reduce Days-In-Inventory from 90+ days to 45 days for non-critical items
- Implement automated reorder points based on usage patterns
- Right-size par levels for surgical kits and cardiac implants

### 3. Process Improvement ($750K savings)
- Standardize preference cards in Surgery and Cardiology
- Implement barcode scanning for expiration date tracking
- Monthly business reviews with department heads

## Skills Demonstrated
✅ **Financial Data Integrity:** GL reconciliation, subledger validation, variance analysis  
✅ **SCM Cost Reduction:** Waste analysis, carrying cost optimization, vendor management  
✅ **Healthcare Operations:** Surgical, Cardiology, Radiology, GI supply chain knowledge  
✅ **Business Intelligence:** Executive dashboards, financial modeling, trend analysis  
✅ **Process Consulting:** Policy development, margin improvement, risk mitigation  

## How to Run
1. Generate data: `python generate_healthcare_data.py`
2. Run analysis: `python financial_analysis.py`
3. Review SQL queries in `sql_queries.sql` for GL reconciliation logic

## Contact
Sri Harshavardhan Josyula  
harshajosyula75@gmail.com  
[LinkedIn](https://www.linkedin.com/in/harsha-vardhan-josyula)
