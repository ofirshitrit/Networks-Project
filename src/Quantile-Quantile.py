import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import laplace, probplot

# Load the CSV file into a pandas DataFrame
path = '/home/ofr/PycharmProjects/FinalProject/resources/csvFiles/Text.csv'
data = pd.read_csv(path)

# Convert "Time" column to float
data['Time'] = data['Time'].astype(float)

# Extract transition delay values and normalize them to [0, 1]
transition_delays = np.diff(data['Time'])  # Calculate inter-event time differences
min_delay = min(transition_delays)
max_delay = max(transition_delays)
normalized_delays = [(delay - min_delay) / (max_delay - min_delay) for delay in transition_delays]
print(normalized_delays)

# Fit a Laplace distribution to the normalized data
loc, scale = laplace.fit(transition_delays)

# Generate a Q-Q plot
plt.figure(figsize=(10, 6))
probplot(normalized_delays, dist=laplace(loc=loc, scale=scale), plot=plt)

plt.xlabel('Theoretical Quantiles (Laplacian Distribution)')
plt.ylabel('Sample Quantiles (Normalized Transition Delay)')
plt.title('Q-Q Plot of Normalized Transition Delay vs Fitted Laplacian Distribution')
# plt.grid(True)
plt.show()
