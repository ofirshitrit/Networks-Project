import csv
import matplotlib.pyplot as plt

# Lists to store the data
time_list = []
length_list = []
protocol_list = []

# Read data from the CSV file
path = '/home/ofr/PycharmProjects/FinalProject/resources/csvFiles/Noise.csv'
with open(path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        time = float(row['Time'])
        length = int(row['Length'])
        protocol = row['Protocol']
        time_list.append(time)
        length_list.append(length)
        protocol_list.append(protocol)

# Set up bin parameters
num_bins = 20  # Number of bins
bin_range = (min(time_list), max(time_list))  # Range for the bins

# Create bins and plot the histogram
plt.figure(figsize=(10, 6))

# Plot data with "TLSv1.2" or "TCP" protocol in red
plt.hist(
    [length_list[i] for i in range(len(protocol_list)) if protocol_list[i] in ["TLSv1.2", "TCP"]],
    bins=num_bins,
    range=bin_range,
    color='red',
    alpha=0.7,
    label='whatsapp'
)

# Plot data with other protocols in blue
plt.hist(
    [length_list[i] for i in range(len(protocol_list)) if protocol_list[i] not in ["TLSv1.2", "TCP"]],
    bins=num_bins,
    range=bin_range,
    color='blue',
    alpha=0.7,
    label='youtube'
)

plt.title('Histogram of Length vs Time')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.legend()
plt.show()