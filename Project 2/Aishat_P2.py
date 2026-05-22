import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
file_name = r"C:\Users\DELL\python.py\MydataAnalysisProject\DecodeLabs_Intern\Project 2\Dataset for Data Analytics (1).xlsx"
df = pd.read_excel(file_name)

print("==================================================")
print("             DATASET STRUCTURE                    ")
print("==================================================")
print(f"Total Transactions (Rows): {df.shape[0]}")
print(f"Total Features (Columns): {df.shape[1]}")
print("\nColumns in this dataset:")
print(list(df.columns))
print("\n")

print("==================================================")
print("   DESCRIPTIVE STATISTICS (FIVE-NUMBER SUMMARY)   ")
print("==================================================")
target_columns = ['Quantity', 'UnitPrice', 'TotalPrice', 'ItemsInCart']
summary_stats = df[target_columns].describe()
print(summary_stats)
print("\n")

print("==================================================")
print("         SHAPE OF DATA DISTRIBUTIONS              ")
print("==================================================")
for col in ['UnitPrice', 'TotalPrice']:
    mean_val = df[col].mean()
    median_val = df[col].median()
    skew_val = df[col].skew()
    
    print(f"--- {col} ---")
    print(f"Mean (Average): ${mean_val:,.2f}")
    print(f"Median (Middle Value): ${median_val:,.2f}")
    print(f"Skewness Score: {skew_val:.2f}")
    
    if skew_val > 0.5:
        print("Result: Right-Skewed (Positively Skewed). High-value outlier orders are pulling the mean up.")
    elif skew_val < -0.5:
        print("Result: Left-Skewed (Negatively Skewed).")
    else:
        print("Result: Symmetrical Distribution. Data is evenly spread.")
    print("-" * 30)
print("\n")

# Set a clean, professional aesthetic for graphics
sns.set_theme(style="whitegrid")

# ==================================================
#   VISUAL 1: DATA DISTRIBUTION HISTOGRAMS
# ==================================================
print("Generating Distribution Plots...")
fig1, axes1 = plt.subplots(1, 2, figsize=(14, 5))

# Plot Unit Price (Symmetrical Distribution)
sns.histplot(df['UnitPrice'], kde=True, color='royalblue', ax=axes1[0], bins=20)
axes1[0].set_title('Unit Price Distribution\n(Symmetrical / Even Spread)', fontsize=13, pad=10)
axes1[0].set_xlabel('Unit Price ($)', fontsize=11)
axes1[0].set_ylabel('Count of Items', fontsize=11)

# Plot Total Price (Right-Skewed Distribution)
sns.histplot(df['TotalPrice'], kde=True, color='crimson', ax=axes1[1], bins=20)
axes1[1].set_title('Total Order Price Distribution\n(Right-Skewed by High-Value Orders)', fontsize=13, pad=10)
axes1[1].set_xlabel('Total Price ($)', fontsize=11)
axes1[1].set_ylabel('Count of Transactions', fontsize=11)

plt.tight_layout()
plt.savefig('data_distributions.png', dpi=300)

# ==================================================
#   VISUAL 2: FIVE-NUMBER SUMMARY BOX PLOT
# ==================================================
print("Generating Five-Number Summary Box Plot...")
fig2, ax2 = plt.subplots(figsize=(10, 5))

# To create a horizontal boxplot for Total Price
sns.boxplot(
    x=df['TotalPrice'], 
    color='lightseagreen', 
    width=0.4, 
    ax=ax2, 
    flierprops={"marker": "o", "markerfacecolor": "crimson", "markeredgecolor": "crimson"}
)

# Setting titles and axis labels
ax2.set_title('Total Order Value: Five-Number Summary & Outlier Map', fontsize=14, pad=15)
ax2.set_xlabel('Total Transaction Value ($)', fontsize=12)

# Annotating key statistical markers directly based on my Terminal Output results
ax2.text(11, 0.25, 'Min\n$11.39', color='black', ha='center', fontweight='bold')
ax2.text(410, -0.25, 'Q1\n$410.52', color='blue', ha='center')
ax2.text(823, 0.28, 'Median\n$823.62', color='darkgreen', ha='center', fontweight='bold')
ax2.text(1578, -0.25, 'Q3\n$1,578.48', color='blue', ha='center')
ax2.text(3456, -0.15, 'Max Outlier\n$3,456.40', color='crimson', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('total_price_boxplot.png', dpi=300)
plt.show()