import matplotlib.pyplot as plt

# Sample data for emotional well-being initiatives
initiatives = ['Inclusive Workplace Culture', 'Recognition Programs', 'Mental Health Support']
initiative_scores = [9, 8, 7]  # Scores (1-10) indicating the effectiveness of each initiative

# Create a bar chart to visualize the effectiveness of emotional well-being initiatives
plt.figure(figsize=(8, 6))
plt.bar(initiatives, initiative_scores, color='lightcoral')
plt.title('Effectiveness of Emotional Well-Being Initiatives')
plt.xlabel('Initiative')
plt.ylabel('Effectiveness (Score)')
plt.ylim(0, 10)  # Set the y-axis limit to 0-10
plt.tight_layout()

# Show the bar chart
plt.show()
