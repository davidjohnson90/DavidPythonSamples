import pandas as pd
import random
import matplotlib.pyplot as plt

# Create a sample dataframe with community engagement data
random.seed(0)
num_initiatives = 50

data = {
    'InitiativeID': range(1, num_initiatives + 1),
    'InitiativeName': [f'Initiative {i}' for i in range(1, num_initiatives + 1)],
    'Category': [random.choice(['Philanthropy', 'Volunteerism', 'Partnerships']) for _ in range(num_initiatives)],
    'Impact': [random.randint(1, 5) for _ in range(num_initiatives)]  # 1=Low, 5=High
}

df = pd.DataFrame(data)

# Calculate and visualize community engagement initiatives
initiative_categories = df['Category'].value_counts()
initiative_impact = df.groupby('Category')['Impact'].mean()

# Visualize initiative categories
plt.figure(figsize=(12, 5))

# Subplot 1: Initiative Categories
plt.subplot(1, 2, 1)
plt.bar(initiative_categories.index, initiative_categories.values, color=['blue', 'green', 'orange'])
plt.title('Community Engagement Initiative Categories')
plt.xlabel('Category')
plt.ylabel('Number of Initiatives')

# Subplot 2: Initiative Impact by Category
plt.subplot(1, 2, 2)
plt.bar(initiative_impact.index, initiative_impact.values, color=['blue', 'green', 'orange'])
plt.title('Average Impact by Initiative Category')
plt.xlabel('Category')
plt.ylabel('Average Impact (1=Low, 5=High)')

plt.tight_layout()
plt.show()
