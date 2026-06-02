import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ==============================
# CREATE OUTPUT FOLDER
# ==============================
Path("visualizations").mkdir(exist_ok=True)

# ==============================
# LOAD DATASET
# ==============================
try:
    df = pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\Internship\sales_data.csv")

    print("Dataset Loaded Successfully!")

    # ==============================
    # DATA CLEANING
    # ==============================
    df.drop_duplicates(inplace=True)

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    df["Month"] = df["Date"].dt.month_name()
    df["Year"] = df["Date"].dt.year

    sns.set_style("whitegrid")

    # ==============================
    # CHART 1 - BAR CHART
    # Revenue by Product
    # ==============================
    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))
    sns.barplot(
        x=product_sales.index,
        y=product_sales.values
    )

    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()

    plt.savefig(
        "visualizations/revenue_by_product.png"
    )
    plt.close()

    # ==============================
    # CHART 2 - PIE CHART
    # Regional Sales
    # ==============================
    regional_sales = (
        df.groupby("Region")["Total_Sales"]
        .sum()
    )

    plt.figure(figsize=(7, 7))

    plt.pie(
        regional_sales,
        labels=regional_sales.index,
        autopct="%1.1f%%"
    )

    plt.title("Regional Sales Distribution")

    plt.savefig(
        "visualizations/regional_sales.png"
    )
    plt.close()

    # ==============================
    # CHART 3 - BOX PLOT
    # ==============================
    plt.figure(figsize=(8, 5))

    sns.boxplot(
        x="Product",
        y="Total_Sales",
        data=df
    )

    plt.title("Sales Distribution by Product")

    plt.tight_layout()

    plt.savefig(
        "visualizations/boxplot_sales.png"
    )

    plt.close()

    # ==============================
    # CHART 4 - HEATMAP
    # ==============================
    numeric_df = df.select_dtypes(
        include="number"
    )

    plt.figure(figsize=(8, 5))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        "visualizations/heatmap.png"
    )

    plt.close()

    # ==============================
    # CHART 5 - LINE CHART
    # Monthly Trend
    # ==============================
    monthly_sales = (
        df.groupby("Month")["Total_Sales"]
        .sum()
    )

    plt.figure(figsize=(10, 5))

    sns.lineplot(
        x=monthly_sales.index,
        y=monthly_sales.values,
        marker="o"
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "visualizations/monthly_trend.png"
    )

    plt.close()

    # ==============================
    # CHART 6 - VIOLIN PLOT
    # ==============================
    plt.figure(figsize=(8, 5))

    sns.violinplot(
        x="Product",
        y="Total_Sales",
        data=df
    )

    plt.title("Product Sales Distribution")

    plt.tight_layout()

    plt.savefig(
        "visualizations/violin_plot.png"
    )

    plt.close()

    # ==============================
    # CHART 7 - HISTOGRAM
    # ==============================
    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["Total_Sales"],
        bins=10,
        kde=True
    )

    plt.title("Sales Frequency Distribution")
    plt.xlabel("Total Sales")

    plt.tight_layout()

    plt.savefig(
        "visualizations/sales_histogram.png"
    )

    plt.close()

    # ==============================
    # DASHBOARD SUMMARY
    # ==============================
    total_revenue = df["Total_Sales"].sum()
    average_sale = df["Total_Sales"].mean()

    best_product = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .idxmax()
    )

    print("\n===== DASHBOARD SUMMARY =====")
    print(f"Total Revenue: ₹{total_revenue:,.2f}")
    print(f"Average Sale: ₹{average_sale:,.2f}")
    print(f"Best Product: {best_product}")
    print("=============================")

    print("\nCharts saved in visualizations folder.")

except FileNotFoundError:
    print("Error: sales_data.csv not found.")

except Exception as e:
    print("Error:", e)