import pandas as pd

# Update this path to make sure it matches your computer's exact file location
path = r"C:\Users\DELL\python.py\MydataAnalysisProject\DecodeLabs_Intern\Project 2\Dataset for Data Analytics (1).xlsx"

try:
    # Attempt to load the data file
    df_decode = pd.read_excel(path)
    
    print("Success! The DecodeLabs dataset is loaded.")
    print("-" * 30)
    print(df_decode.head()) # Shows the first 5 rows
    
    # FOR DATA INTEGRITY
    print("-" * 30)
    print(f"Initial row count: {len(df_decode)}")
    print(f"Duplicate OrderIDs: {df_decode['OrderID'].duplicated().sum()}")
    print(f"Missing values:\n{df_decode.isnull().sum()}")
    print("-" * 30)

    # 1. Standardize Date Format (ISO 8601: YYYY-MM-DD)
    df_decode['Date'] = pd.to_datetime(df_decode['Date']).dt.strftime('%Y-%m-%d')

    # 2. Text Standardization 
    df_decode['Product'] = df_decode['Product'].str.strip().str.title()
    df_decode['PaymentMethod'] = df_decode['PaymentMethod'].str.strip().str.title()

    # 3. Handle Missing Coupon Codes (The 309 missing values)
    df_decode['CouponCode'] = df_decode['CouponCode'].fillna('No Coupon')

    # 4. Ensure TotalPrice is in 2 decimals places
    df_decode['TotalPrice'] = df_decode['TotalPrice'].round(2)

    # Save the final cleaned version for submission
    output_path = r"C:\Users\DELL\python.py\MydataAnalysisProject\DecodeLabs_Intern\Aishat_Umar_Project1_Cleaned.csv"
    df_decode.to_csv(output_path, index=False)

    print("Project 1 Cleaning Complete!")
    print(f"Cleaned file saved to: {output_path}")
    print("-" * 30)
    print(df_decode[['OrderID', 'Date', 'Product', 'TotalPrice']].head())

except FileNotFoundError:
    print(f"ERROR: Could not find the file at path: {path}")
    print("Please check if the file name has a '(1)' or if it is inside a 'Project 2' sub-folder.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")