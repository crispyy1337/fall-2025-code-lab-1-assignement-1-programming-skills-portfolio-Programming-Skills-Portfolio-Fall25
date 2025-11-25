def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


def main():
    num = int(input("Enter a number: "))   # Ask user for a number
    result = check_even_odd(num)           # Pass number to the function
    print(result)                          # Print the returned message


if __name__ == "__main__":
    main()
