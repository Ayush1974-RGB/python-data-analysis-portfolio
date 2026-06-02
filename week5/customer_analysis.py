import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

try:
    # ==========================
    # LOAD DATASETS
    # ==========================
    sales_df = pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\Internship\sales_data.csv")
    customer_df = pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\Internship\customer_churn.csv")

    print("=" * 50)
    print("CUSTOMER SALES ANALYSIS DASHBOARD")
    print("=" * 50)

    # ==========================
    # DATA EXPLORATION
    # ==========================
    print("\nSales Dataset Shape:")
    print(sales_df.shape)

    print("\nCustomer Dataset Shape:")
    print(customer_df.shape)

    # ==========================
    # CHECK MISSING VALUES
    # ==========================
    print("\nMissing Values in Sales Data:")
    print(sales_df.isnull().sum())

    print("\nMissing Values in Customer Data:")
    print(customer_df.isnull().sum())

    # Fill missing values if any
    sales_df.fillna(0, inplace=True)
    customer_df.fillna("Unknown", inplace=True)

    # Remove duplicates
    sales_df.drop_duplicates(inplace=True)
    customer_df.drop_duplicates(inplace=True)

    # ==========================
    # DATE CONVERSION
    # ==========================
    sales_df["Date"] = pd.to_datetime(
        sales_df["Date"],
        errors="coerce"
    )

    sales_df["Year"] = sales_df["Date"].dt.year
    sales_df["Month"] = sales_df["Date"].dt.month_name()
    sales_df["Day"] = sales_df["Date"].dt.day

    # ==========================
    # STRING OPERATIONS
    # ==========================
    sales_df["Product"] = (
        sales_df["Product"]
        .str.strip()
        .str.title()
    )

    sales_df["Region"] = (
        sales_df["Region"]
        .str.strip()
        .str.title()
    )

    # ==========================
    # BASIC METRICS
    # ==========================
    total_revenue = sales_df["Total_Sales"].sum()
    avg_sale = sales_df["Total_Sales"].mean()
    highest_sale = sales_df["Total_Sales"].max()
    lowest_sale = sales_df["Total_Sales"].min()

    print("\n")
    print("=" * 50)
    print("KEY METRICS")
    print("=" * 50)

    print(f"Total Revenue: ₹{total_revenue:,.2f}")
    print(f"Average Sale: ₹{avg_sale:,.2f}")
    print(f"Highest Sale: ₹{highest_sale:,.2f}")
    print(f"Lowest Sale: ₹{lowest_sale:,.2f}")

    # ==========================
    # AGGREGATION 1
    # MONTHLY SALES
    # ==========================
    monthly_sales = (
        sales_df.groupby("Month")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTop Monthly Sales:")
    print(monthly_sales)

    # ==========================
    # AGGREGATION 2
    # PRODUCT SALES
    # ==========================
    product_sales = (
        sales_df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nProduct Revenue:")
    print(product_sales)

    # ==========================
    # AGGREGATION 3
    # REGIONAL SALES
    # ==========================
    regional_sales = (
        sales_df.groupby("Region")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nRegional Revenue:")
    print(regional_sales)

    # ==========================
    # TOP CUSTOMERS
    # ==========================
    top_customers = (
        sales_df.groupby("Customer_ID")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\nTop 10 Customers:")
    print(top_customers)

    # ==========================
    # MULTIPLE CONDITION FILTER
    # ==========================
    high_value_sales = sales_df[
        (sales_df["Total_Sales"] > 100000)
        & (sales_df["Quantity"] >= 5)
    ]

    print("\nHigh Value Transactions:")
    print(high_value_sales.head())

    # ==========================
    # PIVOT TABLE
    # ==========================
    pivot_table = pd.pivot_table(
        sales_df,
        values="Total_Sales",
        index="Region",
        columns="Product",
        aggfunc="sum",
        fill_value=0
    )

    print("\nPivot Table:")
    print(pivot_table)

    # ==========================
    # CREATE FOLDER
    # ==========================
    Path("visualizations").mkdir(
        exist_ok=True
    )

    # ==========================
    # VISUALIZATION 1
    # BAR CHART
    # ==========================
    plt.figure(figsize=(8, 5))
    product_sales.plot(kind="bar")
    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(
        "visualizations/product_sales.png"
    )
    plt.close()

    # ==========================
    # VISUALIZATION 2
    # PIE CHART
    # ==========================
    plt.figure(figsize=(7, 7))
    regional_sales.plot(
        kind="pie",
        autopct="%1.1f%%"
    )
    plt.title("Regional Revenue Share")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(
        "visualizations/regional_sales.png"
    )
    plt.close()

    # ==========================
    # VISUALIZATION 3
    # LINE CHART
    # ==========================
    monthly_sales.sort_values().plot(
        kind="line",
        marker="o",
        figsize=(8, 5)
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(
        "visualizations/monthly_sales.png"
    )
    plt.close()

    # ==========================
    # VISUALIZATION 4
    # TOP CUSTOMERS
    # ==========================
    plt.figure(figsize=(10, 5))
    top_customers.plot(kind="bar")

    plt.title("Top 10 Customers")
    plt.xlabel("Customer ID")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig(
        "visualizations/top_customers.png"
    )
    plt.close()

    print("\n")
    print("=" * 50)
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 50)

    print("\nCharts saved in:")
    print("visualizations/")

except FileNotFoundError as e:
    print(f"\nFile Not Found: {e}")

except Exception as e:
    print(f"\nError: {e}")