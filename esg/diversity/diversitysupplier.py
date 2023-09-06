import pandas as pd
import random
import matplotlib.pyplot as plt

# Create a sample dataframe with supplier data
random.seed(0)
num_suppliers = 50

data = {
    'SupplierID': range(1, num_suppliers + 1),
    'SupplierName': [f'Supplier {i}' for i in range(1, num_suppliers + 1)],
    'DiversityCategory': [random.choice(['Minority-Owned', 'Women-Owned', 'Veteran-Owned', 'Other']) for _ in range(num_suppliers)]
}

df = pd.DataFrame(data)

# Calculate and visualize supplier diversity
supplier_diversity = df['DiversityCategory'].value_counts()

# Visualize supplier diversity
plt.figure(figsize=(8, 6))
plt.bar(supplier_diversity.index, supplier_diversity.values, color=['blue', 'pink', 'green', 'orange'])
plt.title('Supplier Diversity')
plt.xlabel('Diversity Category')
plt.ylabel('Number of Suppliers')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()
