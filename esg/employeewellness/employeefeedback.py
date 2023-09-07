import matplotlib.pyplot as plt

# Sample data for employee feedback initiatives
initiatives = ['Feedback Surveys', 'Open Communication', 'Actionable Feedback']
initiative_scores = [9, 8, 7]  # Scores (1-10) indicating the effectiveness of each initiative

# Create a bar chart to visualize the effectiveness of employee feedback initiatives
plt.figure(figsize=(8, 6))
plt.bar(initiatives, initiative_scores, color='lightcoral')
plt.title('Effectiveness of Employee Feedback Initiatives')
plt.xlabel('Initiative')
plt.ylabel('Effectiveness (Score)')
plt.ylim(0, 10)  # Set the y-axis limit to 0-10
plt.tight_layout()

# Show the bar chart
plt.show()
