import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the parent directory of the current script (src folder)
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Construct the path to the csvFiles folder
csv_file_path = os.path.join(parent_directory, 'resources', 'csvFiles', 'Noise.csv')

# Read the data into a DataFrame
df = pd.read_csv(csv_file_path)


# Convert "Time" column to numeric (removing "No." and converting to float)
df["Time"] = pd.to_numeric(df["Time"], errors="coerce")

# Create time intervals (adjust the interval size as needed)
time_interval = 0.5  # seconds
df["Time Interval"] = (df["Time"] // time_interval) * time_interval

# Group by time intervals and protocol, then count packets
grouped_df = df.groupby(["Time Interval", "Protocol"]).size().unstack().fillna(0)

# Create a custom color scheme
colors = ["#1f77b4", "#1f77b4"]  # Blue color for TCP and TLSv1.2, same color for both
colors += ["#ff7f0e"] * (len(grouped_df.columns) - len(colors))  # Orange color for others

# Create a bar plot with custom colors
ax = grouped_df.plot(kind="bar", stacked=True, figsize=(10, 6), color=colors)

ax.set_xlabel("Time Interval (seconds)")
ax.set_ylabel("Packet Count")
ax.set_title("Packet Counts Over Time for TCP and TLSv1.2 Packets")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
