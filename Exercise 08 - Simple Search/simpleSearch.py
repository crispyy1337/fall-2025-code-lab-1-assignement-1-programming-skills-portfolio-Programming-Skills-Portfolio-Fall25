# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Search term input
use_input = input("Do you want to enter a search term? (yes/no): ").lower()

if use_input == "yes":
    search_term = input("Enter the name to search for: ")
else:
    search_term = "Sam"   # default search term

# Search for the term
found = False

for name in names:
    if name == search_term:
        found = True
        break

# Output
if found:
    print(f'"{search_term}" was found in the list.')
else:
    print(f'"{search_term}" was NOT found in the list.')
