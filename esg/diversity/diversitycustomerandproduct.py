import pandas as pd
import random
import matplotlib.pyplot as plt

# Create a sample dataframe with product and customer data
random.seed(0)
num_products = 50

data = {
    'ProductID': range(1, num_products + 1),
    'ProductName': [f'Product {i}' for i in range(1, num_products + 1)],
    'CustomerDiversity': [random.choice(['High', 'Medium', 'Low']) for _ in range(num_products)],
    'SocialImpact': [random.choice(['Positive', 'Neutral', 'Negative']) for _ in range(num_products)]
}

df = pd.DataFrame(data)

# Calculate and visualize customer diversity and social impact
customer_diversity = df['CustomerDiversity'].value_counts()
social_impact = df['SocialImpact'].value_counts()

# Visualize customer diversity
plt.figure(figsize=(12, 5))

# Subplot 1: Customer Diversity
plt.subplot(1, 2, 1)
plt.pie(customer_diversity.values, labels=customer_diversity.index, autopct='%1.1f%%',
        colors=['green', 'yellow', 'red'])
plt.title('Customer Diversity')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular

# Subplot 2: Social Impact
plt.subplot(1, 2, 2)
plt.bar(social_impact.index, social_impact.values, color=['blue', 'gray', 'red'])
plt.title('Social Impact of Products')
plt.xlabel('Impact')
plt.ylabel('Count')

plt.tight_layout()
plt.show()
