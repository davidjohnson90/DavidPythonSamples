import random
import matplotlib.pyplot as plt

# Define a list of job applicants with diverse backgrounds
applicants = [
    {'name': 'John Smith', 'gender': 'Male', 'ethnicity': 'Caucasian'},
    {'name': 'Maria Rodriguez', 'gender': 'Female', 'ethnicity': 'Hispanic'},
    {'name': 'Ahmed Khan', 'gender': 'Male', 'ethnicity': 'Asian'},
    {'name': 'Lakshmi Patel', 'gender': 'Female', 'ethnicity': 'Indian'},
    {'name': 'Michael Johnson', 'gender': 'Male', 'ethnicity': 'African American'},
    {'name': 'Sofia Kim', 'gender': 'Female', 'ethnicity': 'Asian'},
]

# Shuffle the list of applicants to randomize the order
random.shuffle(applicants)

# Simulate a hiring process
selected_candidate = random.choice(applicants)

# Calculate the diversity statistics
gender_counts = {'Male': 0, 'Female': 0}
ethnicity_counts = {'Caucasian': 0, 'Hispanic': 0, 'Asian': 0, 'Indian': 0, 'African American': 0}

for applicant in applicants:
    gender_counts[applicant['gender']] += 1
    ethnicity_counts[applicant['ethnicity']] += 1

genders = list(gender_counts.keys())
gender_counts = list(gender_counts.values())

ethnicities = list(ethnicity_counts.keys())
ethnicity_counts = list(ethnicity_counts.values())

# Create bar charts to visualize diversity
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.bar(genders, gender_counts, color='lightblue')
plt.title('Gender Diversity')
plt.xlabel('Gender')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
plt.bar(ethnicities, ethnicity_counts, color='lightgreen')
plt.title('Ethnicity Diversity')
plt.xlabel('Ethnicity')
plt.ylabel('Count')

plt.tight_layout()

# Print the selected candidate
print("Selected Candidate:")
print(f"Name: {selected_candidate['name']}")
print(f"Gender: {selected_candidate['gender']}")
print(f"Ethnicity: {selected_candidate['ethnicity']}")

# Show the bar charts
plt.show()
