import matplotlib.pyplot as plt

# Sample data for health promotion initiatives
initiatives = ['Nutrition Workshops', 'Fitness Challenges', 'Health Screenings']
initiative_scores = [9, 8, 7]  # Scores (1-10) indicating the effectiveness of each initiative

# Create a bar chart to visualize the effectiveness of health promotion initiatives
plt.figure(figsize=(8, 6))
plt.bar(initiatives, initiative_scores, color='lightsalmon')
plt.title('Effectiveness of Health Promotion Initiatives')
plt.xlabel('Initiative')
plt.ylabel('Effectiveness (Score)')
plt.ylim(0, 10)  # Set the y-axis limit to 0-10
plt.tight_layout()

# Show the bar chart
plt.show()
