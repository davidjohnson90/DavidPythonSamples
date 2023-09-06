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
    'Age': [random.randint(22, 65) for _ in range(num_employees)],
    'Race': [random.choice(['White', 'Black', 'Asian', 'Hispanic']) for _ in range(num_employees)],
    'PromotionOpportunity': [random.choice(['High', 'Medium', 'Low']) for _ in range(num_employees)],
    'InclusivityRating': [random.randint(1, 5) for _ in range(num_employees)]  # 1=Low, 5=High
}

df = pd.DataFrame(data)

# Assess and visualize inclusive culture indicators

# Indicator 1: Gender Diversity
gender_diversity = df['Gender'].value_counts()

# Indicator 2: Race Diversity
race_diversity = df['Race'].value_counts()

# Indicator 3: Promotion Opportunities
promotion_opportunities = df['PromotionOpportunity'].value_counts()

# Indicator 4: Inclusivity Rating Distribution
inclusivity_rating_distribution = df['InclusivityRating']

# Visualize the indicators
plt.figure(figsize=(12, 10))

# Subplot 1: Gender Diversity
plt.subplot(2, 2, 1)
plt.bar(gender_diversity.index, gender_diversity.values, color=['blue', 'pink'])
plt.title('Gender Diversity')
plt.xlabel('Gender')
plt.ylabel('Count')

# Subplot 2: Race Diversity
plt.subplot(2, 2, 2)
plt.bar(race_diversity.index, race_diversity.values, color=['red', 'blue', 'green', 'orange'])
plt.title('Race Diversity')
plt.xlabel('Race')
plt.ylabel('Count')

# Subplot 3: Promotion Opportunities
plt.subplot(2, 2, 3)
plt.pie(promotion_opportunities.values, labels=promotion_opportunities.index, autopct='%1.1f%%',
        colors=['green', 'yellow', 'red'])
plt.title('Promotion Opportunities')

# Subplot 4: Inclusivity Rating Distribution
plt.subplot(2, 2, 4)
plt.hist(inclusivity_rating_distribution, bins=5, color='purple', edgecolor='black')
plt.title('Inclusivity Rating Distribution')
plt.xlabel('Inclusivity Rating')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
