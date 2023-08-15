import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def pdf_plot(input_folder, output_folder, bins=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename != 'Noise' and filename.endswith('.csv'):
            file_path = os.path.join(input_folder, filename)
            df = pd.read_csv(file_path)
            df = df.drop(['No.'], axis=1)
            df['Delay'] = pd.to_numeric(df['Time']).diff()

            cleaned = df.dropna(subset=['Delay'])

            counts, edges = np.histogram(cleaned['Delay'], bins=bins, density=True)

            pdf = counts / sum(counts)

            plt.figure(figsize=(10, 6))

            plt.step(edges[:-1], pdf, where='post', color='blue', lw=2, label='PDF')

            rate = 1. / np.mean(df['Delay'])
            width = edges[1] - edges[0]
            scale = max(pdf) / (rate * np.exp(-rate * edges[np.argmax(pdf)]))

            x = np.linspace(0, max(edges), 500)
            y = scale * rate * np.exp(-rate * x)

            plt.plot(x, y, color='red', lw=2, label='Fitted Exp')

            plt.xlabel('Inter-Arrival Time')
            plt.ylabel('Density')
            plt.title('PDF of Inter-Arrival Time and Fitted Exp')
            plt.legend()

            output_filename = os.path.splitext(filename)[0] + '_plot.png'
            output_path = os.path.join(output_folder, output_filename)
            plt.savefig(output_path)

            plt.close()


input_folder = '/home/ofr/PycharmProjects/FinalProject/resources/csvFiles'
output_folder = '/home/ofr/PycharmProjects/FinalProject/res/PDF_plots'
pdf_plot(input_folder,output_folder)
