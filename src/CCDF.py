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


folder_path = '/home/ofr/PycharmProjects/FinalProject/resources/csvFiles'
labels = ['Text', 'Images', 'Videos', 'Files', 'Voices']  # List of labels for different types of messages

plt.figure(figsize=(10, 6))

for filename, label in zip(os.listdir(folder_path), labels):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
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
# plt.grid(True)
plt.show()
