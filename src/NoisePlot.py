import pandas as pd
import matplotlib.pyplot as plt
import os

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv('/home/ofr/PycharmProjects/Networks-Project/resources/csvFiles/Noise.csv')
# Get the parent directory of the current script (src folder)
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Construct the path to the csvFiles folder
csv_path = os.path.join(parent_directory, 'resources', 'csvFiles', 'Noise.csv')


# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# Create a mask for conditions
red_condition = df['Source'].eq('157.240.195.56') | df['Destination'].eq('157.240.195.56')
blue_condition = df['Source'].eq('172.217.22.110') | df['Destination'].eq('172.217.22.110')

# Separate data based on conditions
red_data = df[red_condition]
blue_data = df[blue_condition]

# Create the plot
plt.figure(figsize=(10, 6))
plt.bar(red_data['Time'], red_data['Length'], color='red', alpha=0.5, label='Whatsapp')
plt.bar(blue_data['Time'], blue_data['Length'], color='blue', alpha=0.5, label='Youtube')
plt.xlabel('Time')
plt.ylabel('Length')
plt.title('Packets Length Over Time')
plt.legend()

# Save the plot
output_folder = os.path.join(parent_directory, 'res', 'OtherPlots')
plot_filename = 'NoisePlot'
plot_path = os.path.join(output_folder, plot_filename)
plt.savefig(plot_path)
plt.close()

