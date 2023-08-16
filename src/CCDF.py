import os
import pandas as pd
import matplotlib.pyplot as plt


def calculate_ccdf(data):
    sorted_data = sorted(data, reverse=True)
    total = len(sorted_data)
    ccdf = [(i + 1) / total for i in range(total)]
    return sorted_data, ccdf


def plot_ccdf(sorted_data, ccdf, label):
    plt.plot(sorted_data, ccdf, label=label)

def normalize_data(data):
    normalized_data = [(size - min(data)) / (max(data) - min(data)) for size in data]
    return normalized_data


# Get the parent directory of the current script (src folder)
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Construct the path to the csvFiles folder
csv_files = os.path.join(parent_directory, 'resources', 'csvFiles')
# Navigate to the output folder within the res folder
output_folder = os.path.join(parent_directory, 'res', 'OtherPlots')
labels = ['Text', 'Images', 'Videos', 'Files', 'Voices']  # List of labels for different types of messages

plt.figure(figsize=(10, 6))

for filename, label in zip(os.listdir(csv_files), labels):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_files, filename)
        df = pd.read_csv(file_path)
        message_sizes = df['Length'].tolist()
        normalized_sizes = normalize_data(message_sizes)
        sorted_data, ccdf = calculate_ccdf(normalized_sizes)
        plot_ccdf(sorted_data, ccdf, label=label)

plt.xlim(0, 1)
plt.yscale('log')
plt.xlabel('Message Size')
plt.ylabel('Complementary CDF')
plt.title('CCDF of IM Size Distributions')
plt.legend()

# Save the plot
plot_filename = 'CCDF'
plot_path = os.path.join(output_folder, plot_filename)
plt.savefig(plot_path)
plt.close()
