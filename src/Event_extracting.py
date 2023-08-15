
import csv
import matplotlib.pyplot as plt

# Lists to store the data
time_list = []
length_list = []

# Read data from the CSV file
path = '/home/ofr/PycharmProjects/FinalProject/resources/csvFiles/Mix.csv'
with open(path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        time = float(row['Time'])
        length = int(row['Length'])
        time_list.append(time)
        length_list.append(length)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time_list, length_list, linestyle='-', color='b')
plt.title('Length vs Time')
plt.xlabel('Time')
plt.ylabel('Length')
plt.grid(True)
plt.show()



#
#
#

#
# import pandas as pd
# import os
#
# # Read the CSV file into a pandas DataFrame
# path = '/home/ofr/PycharmProjects/FinalProject/resources/csvFiles/Mix.csv'
# data = pd.read_csv(path)
#
# # Extract the unique numbers from the specified column
# unique_numbers = data['Length'].unique()
#
# unique_numbers.sort()
#
# # Print the unique numbers
# for num in unique_numbers:
#     print(num, end=' ')
#
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
#
# folder_path = '/home/ofr/PycharmProjects/FinalProject/resources/csvFiles'
#
# # List all files in the directory
# csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv') and file not in ['Noise.csv', 'Mix.csv']]
# avg_size_packets = []
#
# # Process each CSV file
# for csv_file in csv_files:
#     csv_path = os.path.join(folder_path, csv_file)
#     # Extract the name of the file (without the extension)
#     file_name = os.path.splitext(csv_file)[0]
#     data = pd.read_csv(csv_path)
#     avg_value = data['Length'].mean()
#     avg_size_packets.append(avg_value)
#
#     column_name = 'Length'
#     column_data = data[column_name]
#
#     # Calculate the range of values in the column
#     column_min = column_data.min()
#     column_max = column_data.max()
#
#     # Print the range
#     print(f"Range of values in '{file_name}': {column_min} to {column_max}")
#
# # Sort the data for plotting
# sorted_data = sorted(zip(csv_files, avg_size_packets), key=lambda x: x[1])
#
# # Unzip the sorted data
# sorted_csv_files, sorted_avg_size_packets = zip(*sorted_data)
#
# # Plotting
# plt.figure(figsize=(10, 6))
# plt.plot(sorted_csv_files, sorted_avg_size_packets, marker='o', linestyle='-', color='blue')
# plt.xlabel('CSV Files')
# plt.ylabel('Average Packet Size')
# plt.title('Average Packet Size for Each CSV File')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
#
# # Show the plot
# plt.show()
#
#




