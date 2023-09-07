import matplotlib.pyplot as plt

# Create a sample dataframe with carbon offset project data
projects = ['Reforestation', 'Afforestation', 'Renewable Energy', 'Carbon Capture']
offsets = [8000, 7500, 6000, 7000]  # Carbon offset in metric tons CO2e

# Visualize carbon offset projects
plt.figure(figsize=(8, 6))
plt.barh(projects, offsets, color='green')
plt.title('Carbon Offset Projects')
plt.xlabel('Carbon Offset (metric tons CO2e)')
plt.ylabel('Projects')
plt.gca().invert_yaxis()  # Invert the y-axis to show the highest offset at the top
plt.tight_layout()
plt.show()
