# Import pandas library
import pandas as pd

# -------------------------------
# Step 1: Load Dataset
# -------------------------------
df = pd.read_csv("sales_data.csv")

print("First 5 Rows")
print(df.head())

# -------------------------------
# Step 2: Explore Dataset
# -------------------------------
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# -------------------------------
# Step 3: Data Cleaning
# -------------------------------

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# -------------------------------
# Step 4: Sales Analysis
# -------------------------------

# Total Revenue
total_revenue = df["Total_Sales"].sum()

# Average Sale
average_sale = df["Total_Sales"].mean()

# Highest Sale
highest_sale = df["Total_Sales"].max()

# Lowest Sale
lowest_sale = df["Total_Sales"].min()

# Best Selling Product
best_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)

best_product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .max()
)

# -------------------------------
# Step 5: Report
# -------------------------------

print("\n===== SALES REPORT =====")

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Sale: ₹{average_sale:,.2f}")
print(f"Highest Sale: ₹{highest_sale:,.2f}")
print(f"Lowest Sale: ₹{lowest_sale:,.2f}")

print(
    f"Best Selling Product: {best_product}"
)

print(
    f"Revenue Generated: ₹{best_product_sales:,.2f}"
)

print("========================")