# Project 2: Exploratory Data Analysis Report

Submitted as part of the DecodeLabs Data Analytics Internship Milestone

## Project Description
This project covers the Exploratory Data Analysis phase for our transactional sales dataset. Moving beyond basic static reporting, this analysis establishes descriptive statistics, evaluates the shape of data distributions, and maps transaction thresholds to isolate high-value revenue drivers and business anomalies.

---

## Core Statistical Metrics

Based on the execution of the descriptive analytics script across all 1,200 transaction rows, the structural summary metrics for the primary numeric features are calculated below:

### Total Price Metrics
- Total Transactions Count: 1,200
- Average Order Value: $1,053.97
- Spread of Value (Standard Deviation): $819.86
- Minimum Order Value: $11.39
- Lower Quartile Threshold (25 percent): $410.52
- Median Order Value (50 percent): $823.62
- Upper Quartile Threshold (75 percent): $1,578.48
- Maximum Order Value: $3,456.40

### Unit Price Metrics
- Average Product Cost: $356.41
- Median Product Cost: $364.21
- Inventory Price Range: From $11.39 minimum up to $699.93 maximum

---

## Key Observations and Data Interpretation

### 1. The Geometry of Distribution
- Unit Price Analysis: The unit cost of individual products displays a balanced spread across the inventory. The calculated Mean sits at $356.41 while the Median sits at $364.21. The resulting Skewness Score of -0.03 indicates a highly symmetrical distribution. This confirms that the company inventory covers low-cost accessories and premium equipment evenly without being heavily weighted toward either extreme.
- Total Price Analysis: Gross transaction values display a different distribution structure. While the median purchase value is $823.62, the structural average is pulled upward to $1,053.97, yielding a positive Skewness Score of 0.89. This mathematically indicates a right-skewed distribution. The business implication is that while the standard customer cart volume is consistently clustered at lower-to-mid price tiers, the total revenue stream is periodically driven by heavy, high-value bulk purchases.

### 2. Identifying Trends and Market Tiers
By utilizing the core quartiles from the Five-Number Summary, the transaction volumes can be cleanly segmented into three operational marketplace tiers:
- Low-Volume Volume Base: Transactions ranging from the absolute floor of $11.39 up to the Q1 threshold of $410.52. This segment represents minor retail consumer baskets or standalone accessory replacements.
- Core Market Engine: Transactions falling between the $410.52 mark and the Q3 threshold of $1,578.48. This represents the core commercial baseline where fifty percent of all historical business transactions take place.
- High-Value Enterprise Segment: High-end orders scaling from $1,578.48 up to the maximum transaction value of $3,456.40.

### 3. Outlier and Anomaly Detection
The maximum recorded transaction value reaches $3,456.40, which stands as a clear statistical outlier situated far beyond the third quartile cutoff line of $1,578.48.

Because individual item unit prices are strictly capped at a maximum of $699.93, achieving an order value near $3,500 is not a function of a single luxury asset. Instead, these outliers are driven by combined customer behaviors: corporate or wholesale accounts ordering maximum item variations and purchasing maximum item quantities during a single checkout cycle.

---

## Generated Visualizations
The analytics script automates the generation and preservation of two visual assets saved directly to the project directory:
1. data_distributions.png: A side-by-side histogram displaying density curves that contrast the near-perfect symmetry of product unit costs against the right-skewed revenue tail of final order totals.
2. total_price_boxplot.png: A horizontal box plot charting the specific distribution boundaries of the dataset, providing visual proof of the five-number boundaries and charting the precise placement of high-value revenue outliers.

---

## How to Run
Run the statistical profiling script to generate summary tables and save distribution plots directly to your machine:

```bash
pip install pandas matplotlib seaborn openpyxl
python Project2/eda_analysis.py