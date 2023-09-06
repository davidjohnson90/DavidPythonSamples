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
    'Race': [random.choice(['White', 'Black', 'Asian', 'Hispanic']) for _ in range(num_employees)],
    'Salary': [random.randint(40000, 100000) for _ in range(num_employees)]
}

df = pd.DataFrame(data)

# Calculate gender and racial pay gaps
gender_pay_gap = df.groupby('Gender')['Salary'].mean()
race_pay_gap = df.groupby('Race')['Salary'].mean()

# Visualize pay gaps
plt.figure(figsize=(12, 5))

# Subplot 1: Gender Pay Gap
plt.subplot(1, 2, 1)
gender_pay_gap.plot(kind='bar', color=['blue', 'pink'])
plt.title('Gender Pay Gap')
plt.xlabel('Gender')
plt.ylabel('Average Salary')

# Subplot 2: Racial Pay Gap
plt.subplot(1, 2, 2)
race_pay_gap.plot(kind='bar', color=['red', 'blue', 'green', 'orange'])
plt.title('Racial Pay Gap')
plt.xlabel('Race')
plt.ylabel('Average Salary')

plt.tight_layout()
plt.show()
