import pandas as pd
import matplotlib.pyplot as plt
import os


# Function to create histogram and plot for a CSV file
def create_histogram(csv_file, output_folder, file_name,num_bins=50):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert "Time" column to numeric values
    df["Time"] = pd.to_numeric(df["Time"])

    # Create the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df["Time"], bins=num_bins, weights=df["Length"], edgecolor='black')
    plt.xlabel("Time")
    plt.ylabel("Length")
    plt.title(f"{file_name} Packets Length Over Time")

    # Save the plot
    plot_filename = os.path.splitext(os.path.basename(csv_file))[0] + '_histogram.png'
    plot_path = os.path.join(output_folder, plot_filename)
    plt.savefig(plot_path)
    plt.close()


# Get the parent directory of the current script (src folder)
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Construct the path to the csvFiles folder
csv_files = os.path.join(parent_directory, 'resources', 'csvFiles')
# Navigate to the output folder within the res folder
output_folder = os.path.join(parent_directory, 'res', 'HistogramsPlots')

# List all files in the directory
csv_files = [file for file in os.listdir(csv_files) if file.endswith('.csv') and file not in ['Noise.csv', 'Mix.csv']]

# Process each CSV file
for csv_file in csv_files:
    csv_path = os.path.join(csv_files, csv_file)
    # Extract the name of the file (without the extension)
    file_name = os.path.splitext(csv_file)[0]
    create_histogram(csv_path, output_folder,file_name)


