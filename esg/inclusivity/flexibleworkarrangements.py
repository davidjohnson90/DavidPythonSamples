import matplotlib.pyplot as plt

# Define the message about flexible work arrangements
flexible_work_message = "At OurCompany, we value diversity and understand that our employees have unique needs. That's why we offer flexible work arrangements, including remote work options and flexible hours. We believe that providing flexibility enables our employees to better balance their work and personal lives, supporting their well-being and productivity."

# Create a visual representation of the flexible work message
plt.figure(figsize=(8, 6))
plt.text(0.5, 0.5, flexible_work_message, ha='center', va='center', fontsize=12, color='darkblue', wrap=True)
plt.axis('off')  # Hide the axis
plt.title('Flexible Work Arrangements at OurCompany')

# Show the flexible work message
plt.show()
