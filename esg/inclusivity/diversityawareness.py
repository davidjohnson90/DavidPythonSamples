import matplotlib.pyplot as plt

# Define categories (e.g., gender, ethnicity, etc.) and their corresponding counts
categories = ['Gender', 'Ethnicity', 'Age', 'Sexual Orientation']
counts = [45, 30, 25, 15]  # Replace with actual counts or percentages

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color='skyblue')
plt.title('Diversity Awareness in OurCompany')
plt.xlabel('Categories')
plt.ylabel('Number of Employees')
plt.tight_layout()

# Add a diversity awareness message
diversity_message = "At OurCompany, we embrace diversity in all its forms. " \
                    "Our team includes individuals from various backgrounds, " \
                    "cultures, and identities, each contributing their unique perspectives."

# Display the diversity awareness message
plt.figtext(0.5, -0.15, diversity_message, wrap=True, horizontalalignment='center', fontsize=10)

# Show the bar chart
plt.show()
