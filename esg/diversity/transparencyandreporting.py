import matplotlib.pyplot as plt
import pandas as pd
import random

# Create a sample dataframe with diversity reporting data
random.seed(0)
num_companies = 50

data = {
    'CompanyID': range(1, num_companies + 1),
    'CompanyName': [f'Company {i}' for i in range(1, num_companies + 1)],
    'TransparencyLevel': [random.choice(['High', 'Medium', 'Low']) for _ in range(num_companies)]
}

df = pd.DataFrame(data)

# Calculate and visualize transparency and reporting
transparency_levels = df['TransparencyLevel'].value_counts()

# Visualize transparency and reporting
plt.figure(figsize=(8, 6))
plt.pie(transparency_levels.values, labels=transparency_levels.index, autopct='%1.1f%%',
        colors=['green', 'yellow', 'red'])
plt.title('Transparency and Reporting on Diversity Initiatives')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
plt.show()
