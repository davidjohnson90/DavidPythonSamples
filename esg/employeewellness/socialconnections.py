import matplotlib.pyplot as plt

# Sample data for social connection initiatives
initiatives = ['Team-Building Activities', 'Social Events', 'Open Communication']
initiative_scores = [8, 9, 7]  # Scores (1-10) indicating the effectiveness of each initiative

# Create a bar chart to visualize the effectiveness of social connection initiatives
plt.figure(figsize=(8, 6))
plt.bar(initiatives, initiative_scores, color='lightgreen')
plt.title('Effectiveness of Social Connection Initiatives')
plt.xlabel('Initiative')
plt.ylabel('Effectiveness (Score)')
plt.ylim(0, 10)  # Set the y-axis limit to 0-10
plt.tight_layout()

# Show the bar chart
plt.show()
