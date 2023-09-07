import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataframe with emissions data
data = {
    'Source': ['Operations', 'Transportation', 'Energy Consumption', 'Supply Chains'],
    'Emissions (metric tons CO2e)': [5000, 2500, 7500, 3000]
}

df = pd.DataFrame(data)

# Calculate and display total emissions
total_emissions = df['Emissions (metric tons CO2e)'].sum()
print(f"Total Carbon Emissions: {total_emissions} metric tons CO2e")

# Display emissions by source
print("\nEmissions by Source:")
print(df)

# Visualize emissions by source
plt.figure(figsize=(8, 6))
plt.bar(df['Source'], df['Emissions (metric tons CO2e)'], color='skyblue')
plt.title('Carbon Emissions by Source')
plt.xlabel('Source')
plt.ylabel('Emissions (metric tons CO2e)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
