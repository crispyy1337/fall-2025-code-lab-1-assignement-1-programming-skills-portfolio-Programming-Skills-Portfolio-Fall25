# Store information in a dictionary
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

# Create dictionary with key-value pairs
person = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print values on separate lines using single print statement
print(person["name"], person["hometown"], person["age"], sep="\n")

# Using try except for input validation
print("\nUSING TRY EXCEPT FOR INPUT VALIDATION\n")
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

while True:
    try:
        age = int(input("Enter your age (as a number): "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")

person = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(person["name"], person["hometown"], person["age"], sep="\n")