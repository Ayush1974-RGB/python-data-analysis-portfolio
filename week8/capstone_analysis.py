
# ==========================================================
# CAPSTONE PROJECT
# Business Intelligence & Market Analysis Dashboard
# Uses:
# 1. customer_churn.csv
# 2. sales_data.csv
# 3. house_prices.csv
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ----------------------------------------------------------
# FOLDERS
# ----------------------------------------------------------
Path("visualizations").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)

# ----------------------------------------------------------
# LOAD DATASETS
# ----------------------------------------------------------
customer_df = pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\Internship\customer_churn.csv")
sales_df = pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\Internship\sales_data.csv")
house_df = pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\Internship\house_prices.csv")

print("="*70)
print("BUSINESS INTELLIGENCE & MARKET ANALYSIS CAPSTONE")
print("="*70)

# ----------------------------------------------------------
# CUSTOMER CHURN ANALYSIS
# ----------------------------------------------------------
print("\nCUSTOMER CHURN ANALYSIS")

customer_df["TotalCharges"] = pd.to_numeric(
    customer_df["TotalCharges"], errors="coerce"
)
customer_df.fillna(0, inplace=True)

churn_rate = customer_df["Churn"].mean() * 100
print(f"Churn Rate: {churn_rate:.2f}%")

print("\nDescriptive Statistics")
print(customer_df[["Tenure","MonthlyCharges","TotalCharges"]].describe())

ci_customer = stats.t.interval(
    0.95,
    len(customer_df)-1,
    loc=customer_df["MonthlyCharges"].mean(),
    scale=stats.sem(customer_df["MonthlyCharges"])
)

churn_yes = customer_df[customer_df["Churn"] == 1]["MonthlyCharges"]
churn_no = customer_df[customer_df["Churn"] == 0]["MonthlyCharges"]

t1, p1 = stats.ttest_ind(churn_yes, churn_no, equal_var=False)

tenure_yes = customer_df[customer_df["Churn"] == 1]["Tenure"]
tenure_no = customer_df[customer_df["Churn"] == 0]["Tenure"]

t2, p2 = stats.ttest_ind(tenure_yes, tenure_no, equal_var=False)

customer_corr = customer_df[
    ["Tenure","MonthlyCharges","TotalCharges","SeniorCitizen"]
].corr(numeric_only=True)

X = customer_df[["MonthlyCharges"]]
y = customer_df["TotalCharges"]

model = LinearRegression()
model.fit(X, y)

pred = model.predict(X)
customer_r2 = r2_score(y, pred)

# Visualizations
plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=customer_df)
plt.title("Customer Churn Distribution")
plt.savefig("visualizations/churn_distribution.png")
plt.close()

plt.figure(figsize=(6,4))
sns.boxplot(x="Churn", y="MonthlyCharges", data=customer_df)
plt.title("Monthly Charges by Churn")
plt.savefig("visualizations/monthly_charges_boxplot.png")
plt.close()

plt.figure(figsize=(6,4))
sns.heatmap(customer_corr, annot=True, cmap="coolwarm")
plt.title("Customer Correlation Heatmap")
plt.savefig("visualizations/churn_heatmap.png")
plt.close()

# ----------------------------------------------------------
# SALES ANALYSIS
# ----------------------------------------------------------
print("\nSALES ANALYSIS")

sales_df["Date"] = pd.to_datetime(sales_df["Date"])
sales_df["Month"] = sales_df["Date"].dt.month_name()

total_revenue = sales_df["Total_Sales"].sum()

product_sales = sales_df.groupby("Product")["Total_Sales"].sum()
regional_sales = sales_df.groupby("Region")["Total_Sales"].sum()
monthly_sales = sales_df.groupby("Month")["Total_Sales"].sum()

best_product = product_sales.idxmax()
best_region = regional_sales.idxmax()

ci_sales = stats.t.interval(
    0.95,
    len(sales_df)-1,
    loc=sales_df["Total_Sales"].mean(),
    scale=stats.sem(sales_df["Total_Sales"])
)

plt.figure(figsize=(7,4))
product_sales.sort_values(ascending=False).plot(kind="bar")
plt.title("Revenue by Product")
plt.tight_layout()
plt.savefig("visualizations/product_revenue.png")
plt.close()

plt.figure(figsize=(6,6))
plt.pie(regional_sales, labels=regional_sales.index, autopct="%1.1f%%")
plt.title("Regional Revenue Share")
plt.savefig("visualizations/regional_sales.png")
plt.close()

plt.figure(figsize=(8,4))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.savefig("visualizations/monthly_sales_trend.png")
plt.close()

# ----------------------------------------------------------
# HOUSE PRICE ANALYSIS
# ----------------------------------------------------------
print("\nHOUSE PRICE ANALYSIS")

print(house_df.describe())

house_corr = house_df[
    ["Area","Bedrooms","Bathrooms","Age","Price"]
].corr()

house_ci = stats.t.interval(
    0.95,
    len(house_df)-1,
    loc=house_df["Price"].mean(),
    scale=stats.sem(house_df["Price"])
)

X_house = house_df[["Area","Bedrooms","Bathrooms","Age"]]
y_house = house_df["Price"]

house_model = LinearRegression()
house_model.fit(X_house, y_house)

house_pred = house_model.predict(X_house)
house_r2 = r2_score(y_house, house_pred)

plt.figure(figsize=(6,4))
sns.histplot(house_df["Price"], kde=True)
plt.title("House Price Distribution")
plt.savefig("visualizations/house_price_distribution.png")
plt.close()

plt.figure(figsize=(6,4))
sns.regplot(x="Area", y="Price", data=house_df)
plt.title("Area vs Price")
plt.savefig("visualizations/area_vs_price.png")
plt.close()

plt.figure(figsize=(6,4))
sns.heatmap(house_corr, annot=True, cmap="viridis")
plt.title("House Correlation Heatmap")
plt.savefig("visualizations/house_heatmap.png")
plt.close()

# ----------------------------------------------------------
# EXECUTIVE DASHBOARD
# ----------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

customer_df["Churn"].value_counts().plot(
    kind="bar", ax=axes[0,0], title="Churn Distribution"
)

product_sales.plot(
    kind="bar", ax=axes[0,1], title="Product Revenue"
)

monthly_sales.plot(
    ax=axes[1,0], title="Monthly Sales Trend"
)

sns.histplot(
    house_df["Price"], ax=axes[1,1], kde=True
)

axes[1,1].set_title("House Price Distribution")

plt.tight_layout()
plt.savefig("visualizations/executive_dashboard.png")
plt.close()

# ----------------------------------------------------------
# REPORTS
# ----------------------------------------------------------
with open("reports/statistical_results.txt", "w") as f:
    f.write("CAPSTONE PROJECT RESULTS\n\n")
    f.write(f"Customer Churn Rate: {churn_rate:.2f}%\n")
    f.write(f"Customer Monthly Charges CI: {ci_customer}\n")
    f.write(f"T-Test Charges p-value: {p1}\n")
    f.write(f"T-Test Tenure p-value: {p2}\n")
    f.write(f"Customer Regression R2: {customer_r2:.4f}\n\n")

    f.write(f"Total Revenue: {total_revenue}\n")
    f.write(f"Best Product: {best_product}\n")
    f.write(f"Best Region: {best_region}\n")
    f.write(f"Sales Revenue CI: {ci_sales}\n\n")

    f.write(f"House Price CI: {house_ci}\n")
    f.write(f"House Regression R2: {house_r2:.4f}\n")

with open("reports/executive_summary.md", "w") as f:
    f.write("# Executive Summary\n\n")
    f.write("- Customer churn analysis completed.\n")
    f.write("- Sales performance analyzed.\n")
    f.write("- House market analysis performed.\n")
    f.write("- Business recommendations can be derived from top products, churn behavior and pricing trends.\n")

print("\nProject Completed Successfully!")
print("Charts saved in visualizations/")
print("Reports saved in reports/")
