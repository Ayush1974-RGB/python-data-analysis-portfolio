import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Create folder
Path("visualizations").mkdir(exist_ok=True)

# ==========================
# LOAD DATA
# ==========================
sales_df = pd.read_csv(r"C:\Users\ayush\OneDrive\Desktop\Internship\sales_data.csv")

# ==========================
# DATA PREPARATION
# ==========================
sales_df["Date"] = pd.to_datetime(
    sales_df["Date"],
    errors="coerce"
)

sales_df.drop_duplicates(inplace=True)

# ==========================
# DESCRIPTIVE STATISTICS
# ==========================
sales = sales_df["Total_Sales"]

mean_sales = sales.mean()
median_sales = sales.median()
mode_sales = sales.mode()[0]
std_sales = sales.std()

print("\n===== DESCRIPTIVE STATISTICS =====")
print(f"Mean: {mean_sales:.2f}")
print(f"Median: {median_sales:.2f}")
print(f"Mode: {mode_sales:.2f}")
print(f"Standard Deviation: {std_sales:.2f}")

# ==========================
# CONFIDENCE INTERVAL
# ==========================
confidence = 0.95

ci = stats.t.interval(
    confidence,
    len(sales)-1,
    loc=np.mean(sales),
    scale=stats.sem(sales)
)

print("\n95% Confidence Interval:")
print(ci)

# ==========================
# CORRELATION ANALYSIS
# ==========================
correlation = sales_df["Quantity"].corr(
    sales_df["Total_Sales"]
)

print("\nCorrelation:")
print(correlation)

# ==========================
# HYPOTHESIS TEST 1
# REGION COMPARISON
# ==========================
north = sales_df[
    sales_df["Region"] == "North"
]["Total_Sales"]

south = sales_df[
    sales_df["Region"] == "South"
]["Total_Sales"]

t_stat, p_value = stats.ttest_ind(
    north,
    south,
    equal_var=False
)

print("\nT-Test North vs South")
print("p-value:", p_value)

# ==========================
# HYPOTHESIS TEST 2
# Quantity vs Mean
# ==========================
t2, p2 = stats.ttest_1samp(
    sales_df["Quantity"],
    sales_df["Quantity"].mean()
)

print("\nOne Sample T-Test")
print("p-value:", p2)

# ==========================
# HYPOTHESIS TEST 3
# ANOVA
# ==========================
groups = [
    group["Total_Sales"].values
    for name, group
    in sales_df.groupby("Region")
]

f_stat, p3 = stats.f_oneway(*groups)

print("\nANOVA Test")
print("p-value:", p3)

# ==========================
# REGRESSION ANALYSIS
# ==========================
X = sales_df[["Quantity"]]
y = sales_df["Total_Sales"]

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

r2 = r2_score(y, predictions)

print("\nRegression Analysis")
print(f"R² Score: {r2:.4f}")

# ==========================
# VISUALIZATION 1
# HISTOGRAM
# ==========================
plt.figure(figsize=(8,5))

sns.histplot(
    sales_df["Total_Sales"],
    kde=True
)

plt.title("Sales Distribution")

plt.savefig(
    "visualizations/sales_distribution.png"
)

plt.close()

# ==========================
# VISUALIZATION 2
# HEATMAP
# ==========================
plt.figure(figsize=(8,5))

sns.heatmap(
    sales_df.select_dtypes(
        include=np.number
    ).corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig(
    "visualizations/correlation_heatmap.png"
)

plt.close()

# ==========================
# VISUALIZATION 3
# REGRESSION
# ==========================
plt.figure(figsize=(8,5))

sns.regplot(
    x="Quantity",
    y="Total_Sales",
    data=sales_df
)

plt.title(
    "Regression: Quantity vs Sales"
)

plt.savefig(
    "visualizations/regression_plot.png"
)

plt.close()

# ==========================
# VISUALIZATION 4
# BOXPLOT
# ==========================
plt.figure(figsize=(8,5))

sns.boxplot(
    x="Region",
    y="Total_Sales",
    data=sales_df
)

plt.title("Sales by Region")

plt.savefig(
    "visualizations/boxplot_regions.png"
)

plt.close()

# ==========================
# SAVE RESULTS
# ==========================
with open(
    "hypothesis_tests_results.txt",
    "w"
) as file:

    file.write(
        f"T-Test p-value: {p_value}\n"
    )

    file.write(
        f"One Sample p-value: {p2}\n"
    )

    file.write(
        f"ANOVA p-value: {p3}\n"
    )

print("\nAnalysis Completed Successfully!")