
# Project 3: Relational Logic & SQL Data Analysis

## Description
This project focuses on the structured data extraction and business intelligence querying phase of our core transactional operations. Moving away from standard spreadsheets, this milestone utilizes an enterprise relational framework (MySQL) to model 1,200 unique customer transaction records. By creating optimized schema layers and deploying single and multi-level aggregations (`GROUP BY`, `SUM`, `AVG`, `WHERE`), this architecture extracts precise data points regarding product line performance, marketing acquisition conversion paths, and high-value wholesale customer thresholds.

---

## Step 1: Database Architecture Initialization
Before running any analytical queries, the database structure and table schema constraints must be initialized. This framework maps the columns from our source CSV data into explicit transactional database types.

```sql
-- 1. Create the database container
CREATE DATABASE IF NOT EXISTS Transactions_db;
USE Transactions_db;

-- 2. Clean out old structures to prevent collision conflicts
DROP TABLE IF EXISTS Transactions;

-- 3. Define production schema constraints
CREATE TABLE Transactions (
    OrderID VARCHAR(50) NOT NULL,
    Date DATE NOT NULL,
    CustomerID VARCHAR(50) NOT NULL,
    Product VARCHAR(100) NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    ShippingAddress VARCHAR(255),
    PaymentMethod VARCHAR(50),
    OrderStatus VARCHAR(50),
    TrackingNumber VARCHAR(50),
    ItemsInCart INT,
    CouponCode VARCHAR(50),
    ReferralSource VARCHAR(50),
    TotalPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderID)
);

```

## Step 2: Analytical SQL Tasks & Verified Business Insights

### Task 1: Corporate Executive Summary Metrics (Basic Aggregation)

Objective: Compute foundational performance metrics across the entire data timeline to evaluate organizational health.

```sql
SELECT 
    COUNT(OrderID) AS Total_Transactions,
    SUM(TotalPrice) AS Total_Revenue,
    ROUND(AVG(TotalPrice), 2) AS Average_Order_Value,
    ROUND(AVG(ItemsInCart), 2) AS Average_Items_Per_Cart
FROM Transactions_db.Transactions;

```

* Verified Database Output:

* Total Transactions: 1,200 records
* Total System Revenue: $1,264,761.96
* Average Order Value: $1,053.97
* Average Items Per Cart: 5.49 items



### Task 2: Product Performance Optimization (Grouping & Aggregation)

Objective: Group inventory items to isolate primary revenue contributors and unit sales velocity.

```sql
SELECT 
    Product,
    COUNT(OrderID) AS Order_Count,
    SUM(Quantity) AS Total_Units_Sold,
    SUM(TotalPrice) AS Gross_Product_Revenue
FROM Transactions_db.Transactions
GROUP BY Product
ORDER BY Gross_Product_Revenue DESC;

```

* Verified Database Output:
* Chair:178 orders | 562 units sold |$195,620.11 gross revenue
* Printer: 181 orders | 542 units sold | $195,612.61 gross revenue
* Laptop: 173 orders | 535 units sold | $192,126.56 gross revenue
* Tablet: 179 orders | 497 units sold | $186,568.95 gross revenue
* Monitor: 163 orders | 480 units sold | $175,651.41 gross revenue
* Desk: 170 orders | 508 units sold | $167,459.93 gross revenue
* Phone: 156 orders | 411 units sold | $151,722.39 gross revenue



### Task 3: High-Value Customer Segmentation (Row-Level Filtering)

* Objective: Filter for premium transactions exceeding $1,500 to segment enterprise-tier checkout accounts.

```sql
SELECT 
    OrderID,
    CustomerID,
    Product,
    TotalPrice,
    OrderStatus
FROM Transactions_db.Transactions
WHERE TotalPrice > 1500.00
ORDER BY TotalPrice DESC;

```

* Verified Database Output:
* Total Volume Tier Data: Exactly 317 premium wholesale rows isolated.
* Peak Order Value: Order `ORD2007789` for a Tablet generating $3,456.40.
* Runner-Up Value: Order `ORD201122` for a Monitor generating $3,390.95.
* High-Value Sub-tier: Followed by Order `ORD200632` (Laptop) at $3,390.80 and Order `ORD200469` (Chair) at $3,384.90.



### Task 4: Channel Acquisition Financial Volatility (Multi-Level Aggregation)

* **Objective:** Map inbound traffic streams against checkout methods to track channels yielding the absolute highest financial volumes.

```sql
SELECT 
    ReferralSource,
    PaymentMethod,
    COUNT(OrderID) AS Conversion_Count,
    SUM(TotalPrice) AS Revenue_By_Channel
FROM Transactions_db.Transactions
GROUP BY ReferralSource, PaymentMethod
ORDER BY Revenue_By_Channel DESC;

```

* Verified Database Output:**
* Top Gross Channel: Email traffic checking out via Debit Card generates $63,656.03 across 59 active conversions.
* Runner-Up Channel: Instagram traffic checking out via Online options generates $62,541.05 across 60 conversions.
* Third Growth Path: Instagram traffic checking out via Cash generates $60,491.51 across 56 conversions.



### Task 5: Acquisition Funnel Efficiency (Volume Optimization)

* Objective: Group across conversion funnels sorting strictly by raw transaction volume to pinpoint our stickiest customer entry paths.

```sql
SELECT 
    ReferralSource,
    PaymentMethod,
    COUNT(OrderID) AS Conversion_Count,
    SUM(TotalPrice) AS Revenue_By_Channel
FROM Transactions_db.Transactions
GROUP BY ReferralSource, PaymentMethod
ORDER BY Conversion_Count DESC;

```

* Verified Database Output:
* Highest Volume Intersection: Instagram paths checking out via Online options yield a peak frequency of 60 unique transactions. (generating $62,541.05).
* Runner-Up Volume Intersection: Email channels checking out via Debit Card account for 59 completed conversions (generating $63,656.03).



## How to Run

To initialize this relational database schema and execute the analytical suite, run the source file configuration inside your MySQL instance or preferred IDE connection (e.g., MySQL Workbench):

```bash
# Connect to your local MySQL server instance via terminal
mysql -u root -p

# Execute the master workspace script
mysql> SOURCE path/to/Project 3/queries.sql;

