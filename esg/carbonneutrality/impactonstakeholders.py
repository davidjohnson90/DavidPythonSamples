import matplotlib.pyplot as plt

# Create a pie chart to represent the positive impact on stakeholders
stakeholders = ['Customers', 'Investors', 'Employees', 'Community']
impact_percentage = [40, 25, 20, 15]  # Impact percentage for each stakeholder

colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon']
explode = (0.1, 0, 0, 0)  # Explode the first slice (Customers)

plt.figure(figsize=(8, 6))
plt.pie(impact_percentage, explode=explode, labels=stakeholders, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.title('Positive Impact of Carbon Neutrality on Stakeholders')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
plt.tight_layout()

# Show the pie chart
plt.show()
