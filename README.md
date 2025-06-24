Economic Sensitivity Radar: Segmenting Retail Stores by Macro Impact
Overview
This project explores how external economic variables such as CPI (Consumer Price Index), Unemployment, and Fuel Price influence the weekly sales performance of Walmart stores. The objective was to segment the stores based on their economic sensitivity using regression analysis and unsupervised clustering techniques, and then visualize these insights using Power BI.

The outcome is a complete analytical framework that not only identifies economic drivers of sales but also profiles stores into meaningful behavioral clusters like "Highly Sensitive" and "Resilient."

What I Did
Data Cleaning and Preparation
The dataset was cleaned in Python using pandas. Weekly_Sales values were converted to numeric, date fields were parsed, and column names were stripped of formatting inconsistencies. The data includes two years of weekly data across 45 Walmart stores.

Regression Modeling
For each store, a linear regression model was run with CPI, Unemployment, and Fuel_Price as independent variables, and Weekly_Sales as the dependent variable. Coefficients and R² values were extracted to understand each store's sensitivity and model strength.

Clustering with KMeans
The coefficients and R² scores were standardized and used to cluster stores into three economic behavior types using the KMeans algorithm. The clusters represented different levels of macroeconomic sensitivity, such as Highly Sensitive, Moderate Sensitivity, and Resilient stores.

Dashboard Development in Power BI
All results were visualized in a structured Power BI dashboard with multiple pages and dynamic interactions. The dashboard includes KPI cards, cluster-wise breakdowns, scatter plots, and count visuals to summarize key findings per cluster.

What I Found
Many stores showed high CPI coefficients but low R², suggesting that while inflation has visible influence, sales patterns are not always fully explained by macro factors alone.

Resilient stores were identified as those with low coefficient values across all variables and low R², indicating stable performance regardless of economic shifts.

Highly Sensitive stores had large positive or negative coefficients with higher R² values, meaning their sales are significantly driven by inflation or unemployment conditions.

The largest cluster was made up of Resilient stores, followed by Highly Sensitive, and a small group that showed Moderate Sensitivity.

Tools and Technologies Used
Python
Used for data cleaning, regression modeling, clustering, and export of analytical results.

Pandas and Scikit-learn
Core libraries used for data manipulation and machine learning (linear regression and KMeans).

Power BI
Used for interactive visualization of cluster insights, economic sensitivity comparisons, and executive-level storytelling.

