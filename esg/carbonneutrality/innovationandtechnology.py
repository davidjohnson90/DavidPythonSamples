import matplotlib.pyplot as plt
import numpy as np

# Generate sample data for innovation, technology, and carbon neutrality efforts
np.random.seed(0)
num_samples = 30

innovation = np.random.randint(1, 11, num_samples)  # Innovation score (1-10)
technology = np.random.randint(1, 11, num_samples)  # Technology score (1-10)
carbon_neutrality = np.random.randint(1, 11, num_samples)  # Carbon neutrality score (1-10)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(innovation, technology, c=carbon_neutrality, cmap='coolwarm', s=100)
plt.title('Innovation, Technology, and Carbon Neutrality')
plt.xlabel('Innovation Score')
plt.ylabel('Technology Score')
plt.colorbar(label='Carbon Neutrality Score')
plt.grid(True)
plt.tight_layout()

# Show the scatter plot
plt.show()
