def get_fibonacci_series(limit):
    fibonacci = []
    first = 0
    second = 1

    while (first <= limit):
        fibonacci.append(first)
        first, second = second, first+second
    return fibonacci

def calculate_factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return factorial

def get_positive_integer():
    while True:
        try:
            number = int(input("Enter a positive integer (N): "))

            if number < 0:
                print("Please enter a non-negative integer.")
            else:
                return number

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    number = get_positive_integer()

    fibonacci = get_fibonacci_series(number)
    factorial = calculate_factorial(number)

    print("\nFibonacci series up to", number)
    print(fibonacci)

    print(f"\nFactorial of {number} is {factorial}")


if __name__ == "__main__":
    main()


