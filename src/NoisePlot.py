import pandas as pd
import matplotlib.pyplot as plt
import os

# Your provided data
# data = """
# "No.","Time","Source","Destination","Protocol","Length","Info"
# # ... (rest of the data)
# """

# Get the parent directory of the current script (src folder)
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Construct the path to the csvFiles folder
data = os.path.join(parent_directory, 'resources', 'csvFiles', 'Noise')

# Read the data into a DataFrame
df = pd.read_csv(pd.compat.StringIO(data))

# Filter for TCP and TLSv1.2 packets
filtered_df = df[df["Protocol"].isin(["TCP", "TLSv1.2"])]

# Convert "Time" column to numeric (removing "No." and converting to float)
filtered_df["Time"] = pd.to_numeric(filtered_df["Time"], errors="coerce")

# Create time intervals (adjust the interval size as needed)
time_interval = 0.5  # seconds
filtered_df["Time Interval"] = (filtered_df["Time"] // time_interval) * time_interval

# Group by time intervals and protocol, then count packets
grouped_df = filtered_df.groupby(["Time Interval", "Protocol"]).size().unstack().fillna(0)

# Create a bar plot
ax = grouped_df.plot(kind="bar", stacked=True, figsize=(10, 6))
ax.set_xlabel("Time Interval (seconds)")
ax.set_ylabel("Packet Count")
ax.set_title("Packet Counts Over Time for TCP and TLSv1.2 Packets")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
