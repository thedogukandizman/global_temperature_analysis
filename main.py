import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Fixed_Global_Temperature_Data.csv")
import os

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, "Fixed_Global_Temperature_Data.csv")

# Load the dataset
try:
    df = pd.read_csv(csv_file_path)
    print("CSV file loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found. Make sure it's in the correct folder.")
    exit()


# Display basic info and statistics
print("Dataset Info:")
df.info()
print("\nBasic Statistics:")
print(df.describe())

# Plot Temperature Anomaly Over the Years
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["Year"], y=df["Temperature_Anomaly_C"], marker='o', linestyle='-')
plt.axhline(y=0, color='red', linestyle='--', label='Baseline (0°C)')
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Global Temperature Anomalies (1900-2023)")
plt.legend()
plt.grid(True)
plt.show()

# Moving Average to Show Trends
df['Moving_Avg'] = df['Temperature_Anomaly_C'].rolling(window=10).mean()
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["Year"], y=df["Moving_Avg"], label='10-Year Moving Average', color='orange')
sns.lineplot(x=df["Year"], y=df["Temperature_Anomaly_C"], alpha=0.3, label='Annual Data')
plt.axhline(y=0, color='red', linestyle='--', label='Baseline (0°C)')
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Global Temperature Anomalies with Trend (1900-2023)")
plt.legend()
plt.grid(True)
plt.show()

print("Analysis complete! Visualizations displayed.")
