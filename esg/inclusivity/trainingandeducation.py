import matplotlib.pyplot as plt

# Define training topics and dates
training_topics = ['Unconscious Bias', 'Cultural Competence', 'Inclusion Best Practices']
training_dates = ['2023-10-10', '2023-11-15', '2023-12-05']  # Replace with actual training dates

# Create a bar chart to visualize training schedule
plt.figure(figsize=(10, 4))
plt.barh(training_topics, [1] * len(training_topics), color='lightblue')
plt.title('Diversity and Inclusion Training Schedule (2023)')
plt.xlabel('Training Dates')
plt.ylabel('Training Topics')
plt.yticks(rotation=0)
plt.xticks([])  # Hide x-axis ticks
plt.tight_layout()

# Print the training schedule
print("Training Schedule (2023):")
for topic, date in zip(training_topics, training_dates):
    print(f"{date}: {topic}")

# Show the training schedule chart
plt.show()
