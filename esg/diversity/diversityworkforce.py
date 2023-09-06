import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Create a sample dataframe with employee data
np.random.seed(0)
num_employees = 1000

data = {
    'EmployeeID': range(1, num_employees + 1),
    'Gender': [random.choice(['Male', 'Female']) for _ in range(num_employees)],
    'Age': [random.randint(22, 65) for _ in range(num_employees)]
}

df = pd.DataFrame(data)

# Calculate diversity metrics
gender_diversity = df['Gender'].value_counts()
age_diversity = df['Age'].describe()

# Display diversity metrics
print("Gender Diversity:")
print(gender_diversity)
print("\nAge Diversity:")
print(age_diversity)

# Visualize gender diversity
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(gender_diversity.index, gender_diversity.values, color=['blue', 'pink'])
plt.title('Gender Diversity')
plt.xlabel('Gender')
plt.ylabel('Count')

# Visualize age diversity
plt.subplot(1, 2, 2)
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Age Diversity')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
