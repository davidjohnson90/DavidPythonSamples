import matplotlib.pyplot as plt

# Sample data for physical health initiatives
initiatives = ['Wellness Programs', 'Gym Facilities', 'Health Insurance']
initiative_scores = [8, 6, 9]  # Scores (1-10) indicating the effectiveness of each initiative

# Create a bar chart to visualize the effectiveness of physical health initiatives
plt.figure(figsize=(8, 6))
plt.bar(initiatives, initiative_scores, color='lightblue')
plt.title('Effectiveness of Physical Health Initiatives')
plt.xlabel('Initiative')
plt.ylabel('Effectiveness (Score)')
plt.ylim(0, 10)  # Set the y-axis limit to 0-10
plt.tight_layout()

# Show the bar chart
plt.show()
