import math
from decimal import Decimal, getcontext


def calculate_e(precision):
    getcontext().prec = precision + 1  # Set precision (+1 for accurate rounding)
    e_approx = sum(Decimal(1) / Decimal(math.factorial(n)) for n in range(precision))
    return e_approx


def main():
    print("This program calculates the value of Euler's number (e) up to N decimal places.")

    # Input validation loop
    while True:
        try:
            n = int(input("Enter the number of decimal places (between 1 and 100): "))
            if 1 <= n <= 100:
                break  # Valid input
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

    e_value = calculate_e(n + 10)  # Calculate with extra precision to avoid rounding errors
    formatted_e = f"{e_value:.{n}f}"  # Format the output to N decimal places
    print(f"Euler's number (e) up to {n} decimal places: {formatted_e}")


if __name__ == "__main__":
    main()
