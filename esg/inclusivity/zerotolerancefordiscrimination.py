import matplotlib.pyplot as plt

# Define key points as data points
points = {
    "Zero Tolerance Policy": 1,
    "Safe & Inclusive Environment": 2,
    "Report Inappropriate Behavior": 3,
    "Confidential Reporting": 4,
}

# Create a visual representation of the key points
plt.figure(figsize=(8, 6))
plt.plot([], [])  # Empty plot for labeling
plt.text(0.1, 4.5, "Zero Tolerance for Discrimination", fontsize=16, fontweight='bold')

# Plot data points
for point, value in points.items():
    plt.scatter(0.2, value, marker='o', s=100, color='darkred')
    plt.text(0.3, value, point, fontsize=12, va='center')

# Customize the plot appearance
plt.xlim(0, 1)
plt.ylim(0, 5)
plt.xlabel('Key Points')
plt.ylabel('Importance')
plt.title('Zero Tolerance for Discrimination Key Points')

# Show the key points about zero tolerance
plt.show()
