import matplotlib.pyplot as plt

# Sample data for stress management initiatives
initiatives = ['Mindfulness Programs', 'Stress-Relief Workshops', 'Flexible Work Options']
initiative_scores = [8, 9, 7]  # Scores (1-10) indicating the effectiveness of each initiative

# Create a bar chart to visualize the effectiveness of stress management initiatives
plt.figure(figsize=(8, 6))
plt.bar(initiatives, initiative_scores, color='lightblue')
plt.title('Effectiveness of Stress Management Initiatives')
plt.xlabel('Initiative')
plt.ylabel('Effectiveness (Score)')
plt.ylim(0, 10)  # Set the y-axis limit to 0-10
plt.tight_layout()

# Show the bar chart
plt.show()
