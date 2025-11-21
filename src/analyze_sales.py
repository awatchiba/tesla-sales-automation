import pandas as pd
import matplotlib.pyplot as plt
import os

# Create visuals folder if it doesn’t exist
os.makedirs("visuals", exist_ok=True)

# Load the data
df = pd.read_csv("tesla_sales.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Total sales by region
sales_by_region = df.groupby('region')['sales'].sum()

plt.figure(figsize=(8,5))
sales_by_region.plot(kind='bar', color='skyblue')
plt.title("Total Tesla Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visuals/sales_by_region.png")
plt.close()

# Monthly trend
df['month'] = df['date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('month')['sales'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Tesla Sales Trend")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/monthly_trend.png")
plt.close()

print("Analysis complete! Check the visuals folder for charts.")
