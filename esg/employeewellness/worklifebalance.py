import matplotlib.pyplot as plt

# Sample data for work-life balance initiatives
initiatives = ['Flexible Work Hours', 'Remote Work Options', 'Paid Time Off Policies']
initiative_scores = [8, 9, 7]  # Scores (1-10) indicating the effectiveness of each initiative

# Create a bar chart to visualize the effectiveness of work-life balance initiatives
plt.figure(figsize=(8, 6))
plt.bar(initiatives, initiative_scores, color='lightsalmon')
plt.title('Effectiveness of Work-Life Balance Initiatives')
plt.xlabel('Initiative')
plt.ylabel('Effectiveness (Score)')
plt.ylim(0, 10)  # Set the y-axis limit to 0-10
plt.tight_layout()

# Show the bar chart
plt.show()
