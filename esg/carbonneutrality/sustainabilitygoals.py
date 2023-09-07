import matplotlib.pyplot as plt
import pandas as pd

# Create a sample dataframe with sustainability goals data
data = {
    'Year': [2020, 2021, 2022, 2023, 2024],
    'Emissions Target (metric tons CO2e)': [5500, 5000, 4500, 4000, 3500]
}

df = pd.DataFrame(data)

# Visualize sustainability goals over time
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Emissions Target (metric tons CO2e)'], marker='o', linestyle='-', color='green')
plt.title('Sustainability Goals for Carbon Emissions Reduction')
plt.xlabel('Year')
plt.ylabel('Emissions Target (metric tons CO2e)')
plt.grid(True)
plt.tight_layout()
plt.show()
