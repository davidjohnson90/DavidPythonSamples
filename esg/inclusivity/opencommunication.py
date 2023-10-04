import matplotlib.pyplot as plt

# Define the message about open communication
open_communication_message = "At OurCompany, we value open and honest communication. We believe that every employee's perspective, concerns, and ideas matter. Our culture encourages individuals to share their thoughts and engage in meaningful dialogue. Together, we create an environment where everyone's voice is heard and respected."

# Create a visual representation of the open communication message
plt.figure(figsize=(8, 6))
plt.text(0.5, 0.5, open_communication_message, ha='center', va='center', fontsize=12, color='darkblue', wrap=True)
plt.axis('off')  # Hide the axis
plt.title('Open Communication at OurCompany')

# Show the open communication message
plt.show()
