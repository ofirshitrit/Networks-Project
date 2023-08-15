import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def custom_pdf_plot(csv_folder, output_dir, num_bins=10):
    for filename in os.listdir(csv_folder):
        if 'Noise' not in filename and filename.endswith('.csv'):
            print(filename)
            file_path = os.path.join(csv_folder, filename)
            data_df = pd.read_csv(file_path)
            data_df = data_df.drop(['No.'], axis=1)
            data_df['Delay'] = pd.to_numeric(data_df['Time']).diff()

            clean_data = data_df.dropna(subset=['Delay'])

            counts, edges = np.histogram(clean_data['Delay'], bins=num_bins, density=True)
            pdf = counts / sum(counts)

            plt.figure(figsize=(10, 6))
            plt.step(edges[:-1], pdf, where='post', color='blue', lw=2, label='PDF')

            mean_delay = 1. / np.mean(data_df['Delay'])
            bin_width = edges[1] - edges[0]
            scale_factor = max(pdf) / (mean_delay * np.exp(-mean_delay * edges[np.argmax(pdf)]))

            x = np.linspace(0, max(edges), 500)
            y = scale_factor * mean_delay * np.exp(-mean_delay * x)

            plt.plot(x, y, color='red', lw=2, label='Fitted Exp')

            plt.xlabel('Inter-Arrival Time')
            plt.ylabel('PDF')
            plt.title('Inter-Arrival Time PDF and Fitted Exp')
            plt.legend()

            output_filename = os.path.splitext(filename)[0] + '_plot.png'
            output_path = os.path.join(output_dir, output_filename)
            plt.savefig(output_path)
            plt.close()


# Get the parent directory of the current script
script_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Define paths for CSV files and output plots
csv_files_folder = os.path.join(script_parent_dir, 'resources', 'csvFiles')
output_plots_folder = os.path.join(script_parent_dir, 'res', 'PDFPlots')

# Call the custom_pdf_plot function
custom_pdf_plot(csv_files_folder, output_plots_folder)
