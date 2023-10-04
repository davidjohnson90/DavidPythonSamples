import matplotlib.pyplot as plt

# Define the message about inclusive leadership
inclusive_leadership_message = "At OurCompany, inclusive leadership is at the heart of our culture. Our leaders are committed to setting a positive example by actively promoting diversity, equity, and inclusion. They champion an environment where every voice is heard, and every employee feels valued and respected."

print(inclusive_leadership_message)

# Create a visual representation of inclusive leadership
plt.figure(figsize=(8, 4))
plt.text(0.5, 0.5, inclusive_leadership_message, ha='center', va='center', fontsize=12, color='darkblue', wrap=True)
plt.axis('off')  # Hide the axis
plt.title('Inclusive Leadership at OurCompany')

# Show the inclusive leadership message
plt.show()
