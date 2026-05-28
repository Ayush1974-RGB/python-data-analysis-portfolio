import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Create folders automatically
# -------------------------------

os.makedirs("visualizations", exist_ok=True)

try:
    # -------------------------------
    # Load Dataset
    # -------------------------------

    df = pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\Internship\sales_data.csv")

    print("Dataset Loaded Successfully\n")

    # -------------------------------
    # Data Cleaning
    # -------------------------------

    print("Missing Values:")
    print(df.isnull().sum())

    df.drop_duplicates(inplace=True)

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Create Month Column
    df["Month"] = df["Date"].dt.strftime("%B")

    # -------------------------------
    # Basic Analysis
    # -------------------------------

    total_revenue = df["Total_Sales"].sum()
    average_sale = df["Total_Sales"].mean()

    print("\nTotal Revenue:", total_revenue)
    print("Average Sale:", average_sale)

    # Best Selling Products
    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nSales By Product")
    print(product_sales)

    # Region Analysis
    region_sales = (
        df.groupby("Region")["Total_Sales"]
        .sum()
    )

    print("\nSales By Region")
    print(region_sales)

    # Monthly Trend
    monthly_sales = (
        df.groupby(df["Date"].dt.month)["Total_Sales"]
        .sum()
    )

    # -------------------------------
    # Visualization 1
    # Bar Chart
    # -------------------------------

    plt.figure(figsize=(8,5))
    product_sales.plot(kind="bar")

    plt.title("Sales by Product Category")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.tight_layout()

    plt.savefig(
        "visualizations/sales_by_product.png"
    )

    plt.show()

    # -------------------------------
    # Visualization 2
    # Line Chart
    # -------------------------------

    plt.figure(figsize=(8,5))
    monthly_sales.plot(
        marker="o",
        linewidth=2
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "visualizations/monthly_sales_trend.png"
    )

    plt.show()

    # -------------------------------
    # Visualization 3
    # Pie Chart
    # -------------------------------

    plt.figure(figsize=(8,8))

    region_sales.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Sales Distribution by Region")
    plt.ylabel("")

    plt.tight_layout()

    plt.savefig(
        "visualizations/sales_distribution.png"
    )

    plt.show()

    print("\nAnalysis Completed Successfully!")

except FileNotFoundError:
    print("Error: Dataset file not found.")

except Exception as e:
    print("Unexpected Error:", e)