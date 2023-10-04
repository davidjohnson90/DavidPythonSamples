import random
import matplotlib.pyplot as plt

# Define ERG names and their member counts
ergs = ['Women in Tech', 'Pride Alliance', 'Young Professionals', 'Cultural Exchange']
member_counts = [50, 30, 40, 60]  # Replace with actual ERG member counts

# Create a bar chart to visualize ERG membership
plt.figure(figsize=(8, 6))
plt.bar(ergs, member_counts, color='lightgreen')
plt.title('Employee Resource Group (ERG) Membership')
plt.xlabel('ERG Name')
plt.ylabel('Number of Members')
plt.xticks(rotation=15, ha='right')  # Rotate ERG names for better visibility
plt.tight_layout()

# Print the list of ERG members for each ERG
for erg in ergs:
    members = [f'Member {i}' for i in range(1, random.randint(10, 21))]  # Generate random member names
    print(f'{erg} Members:')
    for member in members:
        print(f'- {member}')
    print()

# Show the bar chart
plt.show()
