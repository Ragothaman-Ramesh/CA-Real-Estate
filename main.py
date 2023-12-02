import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data Cleaning

# Load the data from an Excel file
data = pd.read_excel('real.xlsx')

# Check for missing values
print(data.isnull().sum())

# Get descriptive statistics for each numerical column
print(data.describe())

data.hist(bins=50, figsize=(20, 15))

# Get the median price for each county_name
median_prices_by_county_name = data.groupby(
    'county_name')['median_listing_price'].median()
print(median_prices_by_county_name)

# Get the correlation between property prices and Days on market
correlation_between_prices_and_days_on_market = data[[
    'median_listing_price', 'median_days_on_market'
]].corr()
print(correlation_between_prices_and_days_on_market)

# Quartiles of median listing price for each county_name
quartiles_median_price_by_county_name = data.groupby(
    'county_name')['median_listing_price'].quantile([0.25, 0.5, 0.75])
print(quartiles_median_price_by_county_name)

# Std dev of median listing price for each county_name
std_median_price_by_county_name = data.groupby(
    'county_name')['median_listing_price'].std()
print(std_median_price_by_county_name)

# Get the maximum and minimum median listing price for each county_name
max_min_median_price_by_county_name = data.groupby(
    'county_name')['median_listing_price'].agg(['min', 'max'])
print(max_min_median_price_by_county_name)

# Plot the median listing price for each county_name
plt.figure(figsize=(4, 2))
plt.plot(median_prices_by_county_name, 'o')
plt.xticks(rotation=90)
plt.xlabel('county_name')
plt.ylabel('Median Listing Price')
plt.title('Median Listing Price by county_name')
plt.show()

# Set style for seaborn plots
sns.set(style="whitegrid")

# Plotting Histograms for Numeric Columns
data.hist(bins=50, figsize=(20, 15))
plt.suptitle("Histograms of Numeric Columns", y=1.02, fontsize=16)
plt.show()

# Boxplot of Median Listing Prices by County
plt.figure(figsize=(15, 8))
sns.boxplot(x='county_name', y='median_listing_price', data=data)
plt.xticks(rotation=45, ha="right")
plt.title('Boxplot of Median Listing Prices by County')
plt.show()

# Time Series Analysis: Median Listing Prices over Time
plt.figure(figsize=(15, 8))
sns.lineplot(x='Year and Month', y='median_listing_price', data=data)
plt.title('Time Series Analysis - Median Listing Prices over Time')
plt.xlabel('Date')
plt.ylabel('Median Listing Price')
plt.show()

# Scatter Plot: Median Listing Price vs. Days on Market
plt.figure(figsize=(12, 8))
sns.scatterplot(x='median_days_on_market', y='median_listing_price', data=data)
plt.title('Scatter Plot: Median Listing Price vs. Days on Market')
plt.xlabel('Median Days on Market')
plt.ylabel('Median Listing Price')
plt.show()

# Pairplot for Selected Variables
selected_vars = ['median_listing_price', 'hotness_score', 'median_days_on_market']
sns.pairplot(data[selected_vars])
plt.suptitle("Pairplot of Selected Variables", y=1.02, fontsize=16)
plt.show()

# Violin Plot: Distribution of Median Listing Prices by County
plt.figure(figsize=(15, 8))
sns.violinplot(x='county_name', y='median_listing_price', data=data)
plt.xticks(rotation=45, ha="right")
plt.title('Violin Plot: Distribution of Median Listing Prices by County')
plt.show()


# Facet Grid: Multiple Histograms for Median Listing Prices by County
g = sns.FacetGrid(data, col='county_name', col_wrap=4, height=4)
g.map(plt.hist, 'median_listing_price', bins=20)
g.set_axis_labels('Median Listing Price', 'Frequency')
g.set_titles(col_template='{col_name}')
plt.suptitle("Multiple Histograms for Median Listing Prices by County", y=1.02, fontsize=16)
plt.show()
