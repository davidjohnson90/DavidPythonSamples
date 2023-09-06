import matplotlib.pyplot as plt

# Sample data for board members' diversity
board_members = [
    {'Gender': 'Male', 'Race': 'White', 'Expertise': 'Finance'},
    {'Gender': 'Male', 'Race': 'Asian', 'Expertise': 'Technology'},
    {'Gender': 'Female', 'Race': 'Black', 'Expertise': 'Legal'},
    {'Gender': 'Male', 'Race': 'White', 'Expertise': 'Marketing'},
    {'Gender': 'Female', 'Race': 'Hispanic', 'Expertise': 'Operations'},
    {'Gender': 'Female', 'Race': 'White', 'Expertise': 'Human Resources'},
    {'Gender': 'Male', 'Race': 'Asian', 'Expertise': 'Technology'},
    {'Gender': 'Male', 'Race': 'Black', 'Expertise': 'Legal'},
    {'Gender': 'Female', 'Race': 'White', 'Expertise': 'Finance'},
    {'Gender': 'Male', 'Race': 'Hispanic', 'Expertise': 'Operations'}
]

# Count the number of board members by gender, race, and expertise
gender_counts = {}
race_counts = {}
expertise_counts = {}

for member in board_members:
    gender = member['Gender']
    race = member['Race']
    expertise = member['Expertise']

    gender_counts[gender] = gender_counts.get(gender, 0) + 1
    race_counts[race] = race_counts.get(race, 0) + 1
    expertise_counts[expertise] = expertise_counts.get(expertise, 0) + 1

# Convert counts dictionaries to lists for plotting
genders = list(gender_counts.keys())
gender_values = list(gender_counts.values())
races = list(race_counts.keys())
race_values = list(race_counts.values())
expertises = list(expertise_counts.keys())
expertise_values = list(expertise_counts.values())

# Plotting the board diversity
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

axs[0].bar(genders, gender_values, color='blue', label='Gender')
axs[0].set_title('Board Gender Diversity')
axs[0].set_ylabel('Number of Board Members')

axs[1].bar(races, race_values, color='green', label='Race')
axs[1].set_title('Board Race Diversity')
axs[1].set_ylabel('Number of Board Members')

axs[2].bar(expertises, expertise_values, color='orange', label='Expertise')
axs[2].set_title('Board Expertise Diversity')
axs[2].set_ylabel('Number of Board Members')

plt.tight_layout()
plt.show()
