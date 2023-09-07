import matplotlib.pyplot as plt

# Sample data for mental health initiatives
initiatives = ['Employee Assistance Programs (EAPs)', 'Stress Management Resources', 'Work-Life Balance']
initiative_scores = [9, 7, 8]  # Scores (1-10) indicating the effectiveness of each initiative

# Create a bar chart to visualize the effectiveness of mental health initiatives
plt.figure(figsize=(8, 6))
plt.bar(initiatives, initiative_scores, color='lightgreen')
plt.title('Effectiveness of Mental Health Initiatives')
plt.xlabel('Initiative')
plt.ylabel('Effectiveness (Score)')
plt.ylim(0, 10)  # Set the y-axis limit to 0-10
plt.tight_layout()

# Show the bar chart
plt.show()
