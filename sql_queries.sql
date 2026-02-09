-- Mayo Clinic Performance Consulting Analyst
-- Healthcare SCM Financial Reconciliation & Analysis Queries

-- 1. GL RECONCILIATION: Subledger to General Ledger Validation
SELECT 
    GL_Account,
    Department,
    COUNT(*) as Transaction_Count,
    SUM(Total_Cost) as Total_Debits,
    SUM(Price_Variance) as Variance_Amount,
    SUM(Total_Cost) + SUM(Price_Variance) as Net_GL_Impact,
    CASE 
        WHEN ABS(SUM(Price_Variance)) > 50000 THEN 'Investigate'
        WHEN ABS(SUM(Price_Variance)) > 10000 THEN 'Review'
        ELSE 'OK'
    END as Reconciliation_Status
FROM healthcare_scm_data
GROUP BY GL_Account, Department
ORDER BY ABS(SUM(Price_Variance)) DESC;

-- 2. COST REDUCTION OPPORTUNITY: Waste Analysis by Priority Departments
SELECT 
    Department,
    Category,
    SUM(Qty_Wasted) as Units_Wasted,
    SUM(Wasted_Value) as Financial_Impact,
    AVG(Wasted_Value/Total_Cost)*100 as Waste_Percentage,
    SUM(Carrying_Cost) as Inventory_Holding_Cost
FROM healthcare_scm_data
WHERE Department IN ('Surgery', 'Cardiology', 'Radiology', 'GI')
GROUP BY Department, Category
HAVING SUM(Wasted_Value) > 10000
ORDER BY SUM(Wasted_Value) DESC;

-- 3. VENDOR PERFORMANCE ANALYSIS (for contract renegotiation)
SELECT 
    Vendor,
    Department,
    SUM(Total_Cost) as Annual_Spend,
    SUM(Wasted_Value) as Total_Waste,
    (SUM(Wasted_Value)/SUM(Total_Cost))*100 as Waste_Rate,
    AVG(Unit_Cost) as Avg_Unit_Cost,
    COUNT(DISTINCT Category) as Categories_Supplied
FROM healthcare_scm_data
GROUP BY Vendor, Department
ORDER BY SUM(Total_Cost) DESC;

-- 4. MONTHLY FINANCIAL TRENDS (for forecasting)
SELECT 
    Month,
    Quarter,
    SUM(Total_Cost) as Monthly_Spend,
    SUM(Used_Value) as Value_Realized,
    SUM(Wasted_Value) as Waste_Amount,
    (SUM(Used_Value)/SUM(Total_Cost))*100 as Efficiency_Rate,
    SUM(Carrying_Cost) as Monthly_Carrying_Cost
FROM healthcare_scm_data
GROUP BY Month, Quarter
ORDER BY Month;

-- 5. HIGH-VALUE ITEM MONITORING (for inventory optimization)
SELECT 
    Category,
    Vendor,
    AVG(Unit_Cost) as Unit_Cost,
    SUM(Qty_Ordered) as Total_Units,
    SUM(Days_In_Inventory) as Total_Days_Inventory,
    AVG(Days_In_Inventory) as Avg_Days_In_Stock,
    SUM(Carrying_Cost) as Total_Carrying_Cost
FROM healthcare_scm_data
WHERE Unit_Cost > 1000  -- High-value items only
GROUP BY Category, Vendor
HAVING AVG(Days_In_Inventory) > 90  -- Excess inventory
ORDER BY Total_Carrying_Cost DESC;

-- 6. DEPARTMENT BUDGET VARIANCE (actual vs standard)
SELECT 
    Department,
    SUM(Total_Cost) as Actual_Spend,
    SUM(Qty_Ordered * (Unit_Cost - (Unit_Cost * 0.05))) as Standard_Cost,  -- 5% variance threshold
    SUM(Price_Variance) as Variance,
    CASE 
        WHEN SUM(Price_Variance) > 0 THEN 'Over Budget'
        ELSE 'Under Budget'
    END as Budget_Status
FROM healthcare_scm_data
GROUP BY Department
ORDER BY SUM(Total_Cost) DESC;
