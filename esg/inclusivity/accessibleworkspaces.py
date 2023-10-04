import matplotlib.pyplot as plt

# Define accessibility checklist items
accessibility_checklist = [
    'Provide wheelchair ramps and accessible entrances.',
    'Ensure accessible restrooms with appropriate signage.',
    'Use ergonomic furniture and adjustable desks.',
    'Ensure websites are screen reader compatible.',
    'Provide captions for video content.',
    'Offer sign language interpretation for meetings and events.',
]

# Create a checklist visualization with a larger plot size
plt.figure(figsize=(8, 10))  # Increase the height of the plot

# Customize the plot appearance
plt.text(0.1, 0.95, "Accessibility Checklist", fontsize=16, fontweight='bold')

# Reposition checklist items with more spacing
for i, item in enumerate(accessibility_checklist, start=1):
    plt.text(0.1, 0.9 - i * 0.07, f"{i}. {item}", fontsize=12, color='darkgreen', wrap=True)

# Customize the plot appearance
plt.axis('off')  # Hide the axis

# Show the accessibility checklist
plt.show()
