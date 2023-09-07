import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataframe with emissions and sustainability data
data = {
    'Year': [2019, 2020, 2021, 2022, 2023],
    'Emissions (metric tons CO2e)': [5000, 4800, 4500, 4200, 4000],
    'Emissions Target (metric tons CO2e)': [5500, 5000, 4500, 4000, 3500]
}

df = pd.DataFrame(data)

# Create a sustainability report
plt.figure(figsize=(12, 6))

# Plot emissions data
plt.subplot(1, 2, 1)
plt.plot(df['Year'], df['Emissions (metric tons CO2e)'], marker='o', linestyle='-', color='blue')
plt.title('Carbon Emissions Over Time')
plt.xlabel('Year')
plt.ylabel('Emissions (metric tons CO2e)')
plt.grid(True)

# Plot emissions targets
plt.subplot(1, 2, 2)
plt.plot(df['Year'], df['Emissions Target (metric tons CO2e)'], marker='o', linestyle='-', color='green')
plt.title('Sustainability Goals for Carbon Emissions Reduction')
plt.xlabel('Year')
plt.ylabel('Emissions Target (metric tons CO2e)')
plt.grid(True)

# Adjust subplots layout
plt.tight_layout()

# Save or display the sustainability report
plt.savefig('sustainability_report.png', dpi=300)  # Save the report as an image
plt.show()
