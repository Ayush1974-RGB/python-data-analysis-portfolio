# Statistical Business Analysis

## Project Overview

Statistical Business Analysis is a data science project developed as part of my internship at **The Developer's Arena**.

The objective of this project is to apply statistical techniques to business data in order to identify patterns, test hypotheses, analyze relationships between variables, and generate actionable business insights.

The project uses Python libraries such as Pandas, NumPy, SciPy, Seaborn, Matplotlib, and Scikit-Learn to perform descriptive statistics, confidence interval estimation, hypothesis testing, correlation analysis, and regression modeling.

---

## Objectives

- Calculate descriptive statistics
- Analyze data distributions
- Perform hypothesis testing
- Calculate confidence intervals
- Measure correlations between variables
- Perform regression analysis
- Generate statistical business insights
- Visualize statistical findings

---

## Technologies Used

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Scikit-Learn
- VS Code
- Git
- GitHub

---

## Project Structure

Statistical-Business-Analysis/
│
├── statistical_analysis.py
├── requirements.txt
├── README.md
├── hypothesis_tests_results.txt
│
├── data/
│   ├── sales_data.csv
│   └── customer_churn.csv
│
├── visualizations/
│   ├── sales_distribution.png
│   ├── correlation_heatmap.png
│   ├── regression_plot.png
│   ├── boxplot_regions.png
│   └── confidence_interval_plot.png
│
└── screenshots/
    ├── terminal_output.png
    ├── regression_analysis.png
    ├── correlation_heatmap.png
    └── hypothesis_tests.png

---

## Dataset Information

### Sales Dataset

Columns:

- Date
- Product
- Quantity
- Price
- Customer_ID
- Region
- Total_Sales

Records: 100

### Customer Churn Dataset

Columns:

- CustomerID
- Tenure
- MonthlyCharges
- TotalCharges
- Churn

Records: 500

---

## Features

### Descriptive Statistics

The project calculates:

- Mean
- Median
- Mode
- Standard Deviation

### Confidence Interval Analysis

Calculates a 95% confidence interval for sales data.

### Correlation Analysis

Measures relationships between:

- Quantity Sold
- Revenue
- Price
- Other numerical variables

### Hypothesis Testing

Three statistical tests are performed:

#### Test 1

Independent T-Test

North Region vs South Region Sales

#### Test 2

One Sample T-Test

Quantity comparison against average quantity

#### Test 3

ANOVA

Regional sales comparison

### Regression Analysis

Linear regression is performed to analyze:

Quantity Sold → Revenue Generated

### Data Visualization

The project creates:

- Histogram
- Correlation Heatmap
- Regression Plot
- Box Plot
- Confidence Interval Visualization

---

## Installation

```

### Open Project Folder

```bash
cd Statistical-Business-Analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python statistical_analysis.py
```

---

## Output Files

### Reports

- hypothesis_tests_results.txt
- statistical_report.md

### Visualizations

- sales_distribution.png
- correlation_heatmap.png
- regression_plot.png
- boxplot_regions.png

---

## Statistical Methods Used

### Descriptive Statistics

Used to summarize and understand sales performance.

### Confidence Intervals

Used to estimate the true population average sales.

### Correlation Analysis

Used to determine relationships between business variables.

### Hypothesis Testing

Used to evaluate statistical significance of business assumptions.

### Regression Analysis

Used to predict sales revenue based on quantity sold.

---

## Business Insights

### Insight 1

Average sales value provides an overview of business performance.

### Insight 2

Strong correlations indicate important business relationships.

### Insight 3

Hypothesis testing determines whether observed differences are statistically significant.

### Insight 4

Regional performance comparison helps identify growth opportunities.

### Insight 5

Regression analysis helps forecast future revenue trends.

---

## Testing Evidence

### Test Case 1

Input:
Valid sales dataset

Expected Result:
Statistical analysis completed successfully

Result:
Passed

---

### Test Case 2

Input:
Missing dataset file

Expected Result:
Error message displayed

Result:
Passed

---

### Test Case 3

Input:
Dataset with duplicate records

Expected Result:
Duplicates removed before analysis

Result:
Passed

---

### Test Case 4

Input:
Invalid date values

Expected Result:
Handled during date conversion

Result:
Passed

---

## Future Improvements

- Multiple Regression Analysis
- Predictive Modeling
- Time Series Forecasting
- Interactive Dashboards
- Customer Segmentation Analysis

---

## Conclusion

This project demonstrates the practical application of statistics in business analytics. Through descriptive statistics, confidence intervals, correlation analysis, hypothesis testing, and regression modeling, valuable insights were extracted from business data. The project provides a strong foundation for advanced data science and machine learning applications while helping develop analytical and decision-making skills.

---

## Author

Ayush Singhal

Internship Project – The Developer's Arena