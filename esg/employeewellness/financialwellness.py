import matplotlib.pyplot as plt

# Sample data for financial wellness initiatives
initiatives = ['Financial Wellness Programs', 'Retirement Plans', 'Financial Counseling']
initiative_scores = [9, 8, 7]  # Scores (1-10) indicating the effectiveness of each initiative

# Create a bar chart to visualize the effectiveness of financial wellness initiatives
plt.figure(figsize=(8, 6))
plt.bar(initiatives, initiative_scores, color='lightblue')
plt.title('Effectiveness of Financial Wellness Initiatives')
plt.xlabel('Initiative')
plt.ylabel('Effectiveness (Score)')
plt.ylim(0, 10)  # Set the y-axis limit to 0-10
plt.tight_layout()

# Show the bar chart
plt.show()
