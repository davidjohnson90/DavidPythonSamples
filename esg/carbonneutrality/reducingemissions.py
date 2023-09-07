import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataframe with emissions reduction data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020],
    'Emissions (metric tons CO2e)': [6000, 5800, 5500, 5200, 4900, 4600]
}

df = pd.DataFrame(data)

# Calculate and display emissions reduction percentage
initial_emissions = df['Emissions (metric tons CO2e)'].iloc[0]
final_emissions = df['Emissions (metric tons CO2e)'].iloc[-1]
emissions_reduction = ((initial_emissions - final_emissions) / initial_emissions) * 100

print(f"Emissions Reduction Percentage: {emissions_reduction:.2f}%")

# Visualize emissions reduction over time
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Emissions (metric tons CO2e)'], marker='o', linestyle='-', color='blue')
plt.title('Emissions Reduction Over Time')
plt.xlabel('Year')
plt.ylabel('Emissions (metric tons CO2e)')
plt.grid(True)
plt.tight_layout()
plt.show()
