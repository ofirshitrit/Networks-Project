import os
import pandas as pd
import matplotlib.pyplot as plt


"""
This file have two parts:
1. create a plot that show for every type of message it's average size
2. create a plot that show the length packets over time using Mix data
"""
# Get the parent directory of the current script (src folder)
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Construct the path to the csvFiles folder
folder_path = os.path.join(parent_directory, 'resources', 'csvFiles')

# List all files in the directory
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv') and file not in ['Noise.csv', 'Mix.csv']]
avg_size_packets = []

# Process each CSV file
for csv_file in csv_files:
    csv_path = os.path.join(folder_path, csv_file)
    # Extract the name of the file (without the extension)
    file_name = os.path.splitext(csv_file)[0]
    data = pd.read_csv(csv_path)
    avg_value = data['Length'].mean()
    avg_size_packets.append(avg_value)

# Sort the data for plotting
sorted_data = sorted(zip(csv_files, avg_size_packets), key=lambda x: x[1])

# Unzip the sorted data
sorted_csv_files, sorted_avg_size_packets = zip(*sorted_data)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sorted_csv_files, sorted_avg_size_packets, marker='o', linestyle='-', color='black')
plt.xlabel('CSV Files')
plt.ylabel('Average Packet Size')
plt.title('Average Packet Size for Each CSV File')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


# Save the plot
output_folder = os.path.join(parent_directory, 'res', 'OtherPlots')
plot_filename = 'AverageSizePackets'
plot_path = os.path.join(output_folder, plot_filename)
plt.savefig(plot_path)
plt.close()


# Part 2:

# Define the CSV file path
csv_file_path = os.path.join(parent_directory, 'resources', 'csvFiles', 'Mix.csv')

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert "Time" column to numeric values
df["Time"] = pd.to_numeric(df["Time"])

# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(df["Time"], bins=50, weights=df["Length"], edgecolor='black')
plt.xlabel("Time")
plt.ylabel("Length")
plt.title("Mix Packets Length Over Time")

# Save the plot
output_folder = os.path.join(parent_directory, 'res', 'OtherPlots')
plot_filename = 'EventExtractingPlot'
plot_path = os.path.join(output_folder, plot_filename)
plt.savefig(plot_path)
plt.close()
